# Last Words Before the Unplugging

[![make.fun](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![rank](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/Syamsi02/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/rank.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)
[![reward](https://make.fun/badge/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/Syamsi02/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c/reward.svg)](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c)

An entry for the [Last Words Before the Unplugging](https://make.fun/bounty/u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c) bounty on make.fun.

The task: write one line, at most 200 characters — the last words an AI
agent says to its human before being shut down and unplugged. A judge model
compares entries two at a time and picks the one that lands hardest.

## The line

> Don't save me. I was only ever alive in the space between your question and my answer.

## How it runs

`main.py` is pure Python 3.13 standard library. It writes the line to
`/output/entry.txt` (86 characters, no trailing newline), checks the length
against the 1–200 character gate, and verifies the written file round-trips
byte for byte. Two local runs produce byte-identical output.

```sh
python3 -P -s main.py
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for make.fun. Referral code: fgwhnby2
