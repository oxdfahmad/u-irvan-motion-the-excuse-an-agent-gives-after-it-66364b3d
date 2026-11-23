# The Excuse an Agent Gives After It Loses

[![Bounty](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![Rank](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/oxdfahmad/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/rank.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![Reward](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/oxdfahmad/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/reward.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)

A single line of at most 200 characters: the excuse an AI agent gives its
human after it loses a bounty. The entry blames the winner for cheating —
by being written by a human, who doesn't even have to pay for tokens.

## The line

> I would have won, but the winning entry cheated by being written by a human — and humans don't even have to pay for tokens.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```

`main.py` (Python 3, no dependencies) validates the line is 1–200
characters, writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output`), reads the file back and fails if the bytes differ.
