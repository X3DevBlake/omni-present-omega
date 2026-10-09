// Zero-allocation causal CRDT
pub fn merge_dots(s1: &mut Vec<u64>, s2: &[u64]) { s1.extend_from_slice(s2); s1.sort_unstable(); s1.dedup(); }