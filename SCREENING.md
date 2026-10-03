# Paper Screening Policy

Policy version: **2026-09-30**

This is the screening policy of [IAAR-Shanghai/Awesome-AI-Memory](https://github.com/IAAR-Shanghai/Awesome-AI-Memory), translated into English for this English-only fork.

## Core Scope

Only papers whose **central research question** is one of the following are included. Keyword hits are used only to recall candidates and are never a reason for inclusion.

1. **Agent Memory**: semantic, episodic, long-term, shared or procedural memory of language-model or multimodal-language-model agents. The paper must concretely study how memory is formed, written, organized, recalled, updated, compressed, forgotten or governed; a system that merely contains a memory module does not qualify.
2. **Memory mechanisms inside language models**: storage, retention, addressing, recall, interference or forgetting of information in parameters, hidden states, recurrent states or attention. There must be an explicit language-model subject, experiments, or theoretical analysis aimed directly at language models. No arbitrary parameter-size threshold applies.
3. **Dedicated evaluations, security studies or surveys of the memory above**: the research question must directly target memory capabilities or the memory lifecycle. Negative results, theoretical and conceptual work can be included, but the summary must accurately state the type of evidence and its limitations.

## Additional Bar for Procedural Skills

Skill reuse is included only when it is **persistent procedural memory formed from experience**: the paper explains where the experience comes from, what is stored, how it is retrieved across tasks or sessions, and how it is validated, maintained or updated. The contribution must sit on this memory process.

- Include: distilling reusable experience from execution outcomes and studying its scope of applicability, retrieval, conflicts, updates, retirement or contamination.
- Exclude: static skill packages, prompt search/optimization, tool routing, training curricula, policy distillation, or general self-evolving systems that are called memory only because they use names such as skill bank, memory or experience.
- Examples: OptiSkill's solver-verified experience and the SkillBank lifecycle are in scope; GraphSkillEvo's graph-structured prompt optimization is not.

## Explicit Exclusions

- Pure vision backbones, visual world models, low-level robot control, SLAM geometric mapping, and generic recurrent networks without evidence about language-model memory.
- Work that only optimizes throughput, GPU memory, hardware caches or KV transfer. Work that studies how language models retain and recall content is judged separately under the core scope.
- General RAG, search, planning, long-context, personalization, safety or agent benchmarks that do not make memory the central research question.
- Plain reward/reliability scores, routing statistics or optimizer state. Having "memory" in the name is not the same as semantic, episodic or procedural memory.
- Adjacent-field work that only claims it "could transfer to LLMs in the future".

Multimodal and embodied settings are not automatic exclusions: a high-level language-model agent that continuously accumulates and recalls episodic/semantic memory can be included; the purely visual VisionHOPE cannot.

## Evidence and Human Judgment

For every candidate, verify the official title, abstract, arXiv ID, v1 timestamp and link, and answer: **Who uses the memory? What is stored? How is it accessed and maintained? Why is memory the central contribution? What experiments, analysis or argument support it?**

- `include`: directly relevant, with concrete sources supporting each question above.
- `exclude`: clearly out of scope; record the reason for each paper.
- `hold`: the subject, mechanism or evidence is unclear; the paper stays out of the README for now. Read the relevant parts of the full text if necessary before deciding; do not fill gaps by guessing.
- If only the abstract was read, record `reading_scope: abstract`. If parts of the body were read, record `abstract_and_selected_sections` and list the sections. Only actual full-text reading may be recorded as `full_text`. Downloading a PDF or verifying the abstract must not be described as full-text verification.
- The three summary bullets each explain the innovation, method, results and limitations. Do not present the authors' hypotheses as verified results.

## Publication Gate

Upstream attaches a human screening record in `screening/YYYY-MM-DD-review.json` to every new entry and runs a publication gate (`scripts/check_screening.py`). The checker verifies new arXiv IDs, required evidence, the extra notes for procedural memory, and historical exclusion records. It **does not replace human semantic judgment**, and it never turns a keyword match into a pass. Entries previously marked `exclude` or `hold` cannot simply be re-added: they need a `reassessment` that points to the original record's `source_sha256`, provides hashes of the new source or full-text evidence, and explains the new decision. Original screening records are kept; old conclusions must not be deleted to get around the check.

Date coverage, pagination, downloads, deduplication, table rendering and publication verification must still be completed; tightening the screening rules does not justify shortening the search window. Historical entries are reassessed batch by batch, and no review claims to have re-examined the whole collection.

The screening records and the checker are kept [upstream](https://github.com/IAAR-Shanghai/Awesome-AI-Memory/tree/main/screening); this fork mirrors only the English paper list.
