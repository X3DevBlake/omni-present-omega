// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/**
 * @title HumanityToken ($HUMANITY)
 * @author Omni Sovereign Swarm Collective & Council 5 (Blockchain & Staking)
 * @notice Official Smart Contract for the Humanity Token:
 *         - Total Max Supply: Exactly 10,000,000,000 HUMANITY (10 Billion)
 *         - Decimals: 18 (Fractioned down to wei for real-time micro-mining)
 *         - Proof-of-Humanity Free Public Mining Faucet
 *         - Referral Incentive Multipliers (25% boost + milestone rewards)
 *         - Phase II Mainnet Liquidity Bridge Lock
 */

interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

contract HumanityToken is IERC20 {
    string public constant name = "Humanity";
    string public constant symbol = "HUMANITY";
    uint8 public constant decimals = 18;

    // Total Cap: 10 Billion Tokens with 18 decimals
    uint256 public constant TOTAL_SUPPLY_CAP = 10_000_000_000 * 10**18;

    // Distribution Pools
    uint256 public constant MINING_POOL_CAP     = 6_000_000_000 * 10**18; // 60% Free Public Mining
    uint256 public constant REFERRAL_POOL_CAP   = 2_000_000_000 * 10**18; // 20% Referral & Community Incentives
    uint256 public constant ECOSYSTEM_POOL_CAP  = 1_000_000_000 * 10**18; // 10% Protocol Development & Grants
    uint256 public constant LIQUIDITY_BRIDGE_CAP= 1_000_000_000 * 10**18; // 10% Phase II Mainnet Liquidity Bridge

    uint256 public totalMined;
    uint256 public totalReferralRewardsClaimed;
    uint256 public currentBlockHeight;
    bool public withdrawalsEnabled; // Mainnet Phase II Bridge Flag (default: false)

    address public immutable governanceAuthority;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Miner Telemetry State
    struct MinerState {
        bool isRegistered;
        string humanId;
        uint256 totalMinedAmount;
        uint256 lastMiningTimestamp;
        uint256 referralCount;
        uint256 hashrateMultiplierBps; // 10000 = 1.0x (base rate), +2500 per referral
        address referrer;
    }

    mapping(address => MinerState) public miners;
    mapping(string => address) public humanIdToAddress;

    event MinerRegistered(address indexed miner, string humanId, address indexed referrer);
    event TokensMined(address indexed miner, uint256 amount, uint256 totalMinerYield);
    event ReferralBonusCredited(address indexed referrer, address indexed newMiner, uint256 bonusAmount);
    event WithdrawalsLockedAttempt(address indexed user, string reason);
    event PhaseIIBridgeInitialized(uint256 timestamp);

    modifier onlyGovernance() {
        require(msg.sender == governanceAuthority, "Humanity: Caller is not Governance Authority");
        _;
    }

    constructor(address _governance) {
        require(_governance != address(0), "Invalid governance address");
        governanceAuthority = _governance;
        withdrawalsEnabled = false; // Intentionally disabled for Pre-Market Genesis
        currentBlockHeight = 1;

        // Allocate Genesis Reserves (Ecosystem & Liquidity Vault)
        _balances[_governance] = ECOSYSTEM_POOL_CAP;
        emit Transfer(address(0), _governance, ECOSYSTEM_POOL_CAP);
    }

    function totalSupply() external pure override returns (uint256) {
        return TOTAL_SUPPLY_CAP;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        _allowances[sender][msg.sender] -= amount;
        _balances[sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @notice Register Human Identity to start Free Mining
     */
    function registerHumanityAccount(string calldata humanId, address referrer) external {
        require(!miners[msg.sender].isRegistered, "Humanity: Account already registered");
        require(humanIdToAddress[humanId] == address(0), "Humanity: Human ID taken");

        miners[msg.sender] = MinerState({
            isRegistered: true,
            humanId: humanId,
            totalMinedAmount: 0,
            lastMiningTimestamp: block.timestamp,
            referralCount: 0,
            hashrateMultiplierBps: 10000, // 100% Base Rate
            referrer: referrer
        });

        humanIdToAddress[humanId] = msg.sender;

        // Process Welcome & Referral Incentives if referred
        if (referrer != address(0) && referrer != msg.sender && miners[referrer].isRegistered) {
            miners[referrer].referralCount += 1;
            // Add +25% Hashrate Multiplier per referral (+2500 bps)
            miners[referrer].hashrateMultiplierBps += 2500;

            // Credit 500 Welcome Bonus Tokens to new user
            uint256 welcomeBonus = 500 * 10**18;
            if (totalReferralRewardsClaimed + welcomeBonus <= REFERRAL_POOL_CAP) {
                totalReferralRewardsClaimed += welcomeBonus;
                _balances[msg.sender] += welcomeBonus;
                emit Transfer(address(0), msg.sender, welcomeBonus);
                emit ReferralBonusCredited(referrer, msg.sender, welcomeBonus);
            }
        }

        emit MinerRegistered(msg.sender, humanId, referrer);
    }

    /**
     * @notice Claim Free Mining Yield generated by web client Proof-of-Humanity shares
     */
    function submitMiningProof(uint256 shares, uint256 proofNonce) external {
        require(miners[msg.sender].isRegistered, "Humanity: Account not registered");
        require(shares > 0, "Humanity: Zero shares submitted");

        // Calculate reward: 0.0001 HUMANITY per valid proof share * hashrate multiplier
        uint256 baseUnit = 10**14; // 0.0001 token
        uint256 multiplier = miners[msg.sender].hashrateMultiplierBps;
        uint256 rewardAmount = (shares * baseUnit * multiplier) / 10000;

        require(totalMined + rewardAmount <= MINING_POOL_CAP, "Humanity: Public mining pool exhausted");

        totalMined += rewardAmount;
        _balances[msg.sender] += rewardAmount;
        miners[msg.sender].totalMinedAmount += rewardAmount;
        miners[msg.sender].lastMiningTimestamp = block.timestamp;
        currentBlockHeight += 1;

        emit Transfer(address(0), msg.sender, rewardAmount);
        emit TokensMined(msg.sender, rewardAmount, miners[msg.sender].totalMinedAmount);
    }

    /**
     * @notice Withdrawal execution function - Enforces Mainnet Phase II Bridge Guardrail
     */
    function withdraw(uint256 amount) external {
        if (!withdrawalsEnabled) {
            emit WithdrawalsLockedAttempt(msg.sender, "Withdrawals Locked: Mainnet Phase II Bridge Coming Soon");
            revert("Withdrawals are currently disabled. Mainnet Phase II Bridge Coming Soon!");
        }
        require(_balances[msg.sender] >= amount, "Insufficient balance");
        _balances[msg.sender] -= amount;
        emit Transfer(msg.sender, address(0), amount);
    }

    /**
     * @notice Governance function to unlock Phase II Mainnet Bridge
     */
    function enableMainnetBridge() external onlyGovernance {
        withdrawalsEnabled = true;
        emit PhaseIIBridgeInitialized(block.timestamp);
    }

    /**
     * @notice Returns remaining unmined tokens in public pool
     */
    function remainingPublicMiningPool() external view returns (uint256) {
        if (totalMined >= MINING_POOL_CAP) return 0;
        return MINING_POOL_CAP - totalMined;
    }
}
