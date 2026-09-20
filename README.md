\# SemanticDedup



SemanticDedup is a standalone GenLayer Intelligent Contract for determining whether two immutable text artifacts are substantially duplicate, distinct, or inconclusive.



It is designed for reusable duplicate-contribution detection across hackathons, grant submissions, DAO proposals, reports, documentation, code-related text artifacts, and other immutable contributions.



\## Why GenLayer



Duplicate detection cannot be reduced reliably to exact hashing or simple string similarity.



Two artifacts may express substantially the same contribution while using different wording, ordering, names, or formatting. Conversely, two artifacts may share terminology or structure while still contain materially distinct work.



SemanticDedup uses GenLayer nondeterministic execution so validators independently compare the verified contents of both artifacts and reach consensus on the semantic verdict.



\## Trust model



SemanticDedup does not trust caller-written summaries.



For each artifact, the caller supplies:



\- validator-accessible HTTPS URI

\- SHA-256 digest of the exact artifact bytes



Validators independently:



1\. fetch the artifact

2\. enforce a 1 MiB size limit

3\. verify SHA-256

4\. decode the artifact as UTF-8

5\. compare the verified contents semantically



\## Verdicts



\- `SUBSTANTIAL\_DUPLICATE`

\- `DISTINCT`

\- `INCONCLUSIVE`



The contract does not infer plagiarism, ownership, fraud, authorship, or intent.



\## Symmetric comparison



Comparison identity is symmetric.



Comparing artifact A with artifact B produces the same comparison ID as comparing artifact B with artifact A.



The comparison ID is derived from a versioned domain separator and the two lexicographically sorted artifact digests.



This prevents duplicate records caused by reversed input ordering.



\## Public API



```text

compare(

&#x20; artifact\_a\_uri,

&#x20; artifact\_a\_sha256,

&#x20; artifact\_b\_uri,

&#x20; artifact\_b\_sha256

)



get\_result(

&#x20; artifact\_a\_sha256,

&#x20; artifact\_b\_sha256

)



get\_record(comparison\_id)



comparison\_id(

&#x20; artifact\_a\_sha256,

&#x20; artifact\_b\_sha256

)



is\_compared(

&#x20; artifact\_a\_sha256,

&#x20; artifact\_b\_sha256

)



list\_comparisons()



contract\_info()



