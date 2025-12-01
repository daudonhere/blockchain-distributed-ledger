# Results
The simulation results indicate the following :

The hash of each block is tightly bound to its internal data.

Modifying a single character within a block produces a completely different hash due to the cryptographic avalanche effect.

Tampering with any block disrupts the validity of the entire chain, causing the validation function to detect inconsistencies instantly.

Blockchain exhibits strong resilience against unauthorized modifications because a single altered block forces recalculation of all subsequent hashes.
Analysis

# Analysis
Scientific analysis shows that Blockchain structures utilize SHA-256 cryptography to build mathematically secure links between blocks, producing :

1. Real-Time Tamper Detection
Any unauthorized data modification is detected immediately across network participants.

2. Inter-Block Dependency
A block’s hash becomes a structural component of the next block, forming a robust chain.

3. High Resistance to Attacks
51% attacks require immense computational resources.
Block tampering demands recomputation of all subsequent hashes, which is computationally infeasible.

4. Global Ledger Consistency
Consensus mechanisms ensure nodes maintain a synchronized and valid version of the blockchain.

https://medium.com/@hellodadedaud/id-evaluasi-ilmiah-struktur-data-blockchain-sebagai-sistem-pencatatan-terdistribusi-modern-2e6efa317443
https://medium.com/@hellodadedaud/en-scientific-evaluation-of-blockchain-data-structures-as-a-modern-distributed-ledger-system-8829dc1794a4
