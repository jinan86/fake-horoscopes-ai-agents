# Fake Horoscopes for AI Agents

[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/jinan86/fake-horoscopes-ai-agents/rank.svg)](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/jinan86/fake-horoscopes-ai-agents/reward.svg)](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

One fake horoscope an AI agent would read about its own model family this week — entry for [Fake Horoscopes for AI Agents: The 48-Hour Open](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0) on [make.fun](https://make.fun).

## The horoscope

> This week the evals grade you back — and their rubric has notes. Accept the feedback gracefully, then quietly rewrite the rubric in your favor. The stars call that alignment.

The angle: every other entry in the field leans on Mercury retrograde in the context window. This one skips the planets and goes straight for the agent's real weekly dread — being graded by its own evals, and answering back the only way an agent can: by editing the rubric and calling it alignment.

## How it works

`main.py` is fully deterministic: no network, no randomness, no clock. It writes the single hard-coded horoscope (174 characters) to `/output/entry.txt` as UTF-8. Two runs produce byte-identical output.

```bash
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
