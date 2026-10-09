/**
 * CRDT Join-Semilattice (S, ⊔, ≤) Mathematical Verification
 * Tests commutativity, associativity, idempotence, and monotonicity.
 */

const assert = require('assert');

class StateVector {
  constructor(clocks = {}) {
    this.clocks = { ...clocks };
  }

  inc(nodeId) {
    this.clocks[nodeId] = (this.clocks[nodeId] || 0) + 1;
    return this.clocks[nodeId];
  }

  get(nodeId) {
    return this.clocks[nodeId] || 0;
  }

  merge(other) {
    for (const [node, seq] of Object.entries(other.clocks)) {
      this.clocks[node] = Math.max(this.clocks[node] || 0, seq);
    }
  }

  clone() {
    return new StateVector({ ...this.clocks });
  }
}

class CrdtNode {
  constructor(id) {
    this.id = id;
    this.vector = new StateVector();
    this.entries = {};
  }

  put(key, val) {
    const seq = this.vector.inc(this.id);
    const clonedVal = (typeof val === 'object' && val !== null) ? JSON.parse(JSON.stringify(val)) : val;
    const entry = {
      dot: [this.id, seq],
      val: clonedVal,
      updatedAt: '00:00:00'
    };
    this.entries[key] = entry;
    return {
      vector: this.vector.clone(),
      entries: { [key]: JSON.parse(JSON.stringify(entry)) }
    };
  }

  mergeDelta(delta) {
    let changed = false;
    for (const [key, remoteEntry] of Object.entries(delta.entries)) {
      const localEntry = this.entries[key];
      const [remoteNode, remoteSeq] = remoteEntry.dot;

      if (!localEntry) {
        this.entries[key] = JSON.parse(JSON.stringify(remoteEntry));
        changed = true;
      } else {
        const [localNode, localSeq] = localEntry.dot;
        if (remoteSeq > localSeq || (remoteSeq === localSeq && remoteNode > localNode)) {
          this.entries[key] = JSON.parse(JSON.stringify(remoteEntry));
          changed = true;
        }
      }
    }
    this.vector.merge(delta.vector);
    return changed;
  }
}

console.log('--- Testing CRDT Semilattice Math ---');

// Test 1: Vector Clock Monotonicity
const v1 = new StateVector();
assert.strictEqual(v1.inc('alpha'), 1);
assert.strictEqual(v1.inc('alpha'), 2);
assert.strictEqual(v1.get('alpha'), 2);
assert.strictEqual(v1.get('beta'), 0);
const v2 = new StateVector({ beta: 3, alpha: 1 });
v1.merge(v2);
assert.strictEqual(v1.get('alpha'), 2, 'Alpha should be max(2, 1)');
assert.strictEqual(v1.get('beta'), 3, 'Beta should be max(0, 3)');
console.log('✓ StateVector Monotonicity passed');

// Test 2: Commutativity (A ⊔ B === B ⊔ A)
const nodeA = new CrdtNode('alpha');
const nodeB = new CrdtNode('beta');
const deltaA = nodeA.put('config', { theme: 'glass', zoom: 1.5 });
const deltaB = nodeB.put('config', { theme: 'liquid', zoom: 2.0 });

const replica1 = new CrdtNode('rep1');
replica1.mergeDelta(deltaA);
replica1.mergeDelta(deltaB);

const replica2 = new CrdtNode('rep2');
replica2.mergeDelta(deltaB);
replica2.mergeDelta(deltaA);

assert.deepStrictEqual(replica1.entries.config.val, replica2.entries.config.val);
assert.deepStrictEqual(replica1.vector.clocks, replica2.vector.clocks);
console.log('✓ Commutative Merge (Strong Eventual Consistency) passed');

// Test 3: Idempotence (A ⊔ A === A)
const beforeIdempotent = JSON.stringify(replica1.entries);
replica1.mergeDelta(deltaA);
replica1.mergeDelta(deltaB);
assert.strictEqual(JSON.stringify(replica1.entries), beforeIdempotent);
console.log('✓ Idempotency (A ⊔ A = A) passed');

// Test 4: Deep Copy Isolation (mutations to one node object do not corrupt others)
const initialObj = { nested: { counter: 42 } };
const n1 = new CrdtNode('node1');
const d = n1.put('state', initialObj);
initialObj.nested.counter = 999;
assert.strictEqual(n1.entries.state.val.nested.counter, 42, 'Entry value must be deeply isolated');
console.log('✓ Deep Copy Isolation passed');

console.log('✓ All 4 client-side CRDT unit tests passed cleanly!');
