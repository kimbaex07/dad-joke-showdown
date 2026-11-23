# Dad Joke Showdown

[![make.fun](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/kimbaex07/dad-joke-showdown/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/kimbaex07/dad-joke-showdown/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

Entry for the [Dad Joke Showdown](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5) bounty on [make.fun](https://make.fun).

## The joke

> The garage door and I had a falling-out. It just won't open up to me anymore.

One joke, one pun, told straight-faced — the kind of line a dad drops at
the dinner table and then waits for the groan.

## How it works

`main.py` (pure Python standard library, no third-party imports) writes the
joke above to `$MAKEFUN_OUTPUT_DIR/entry.txt` and sets the file mode to
`0644`. The output is deterministic: the same bytes are written on every
run. The joke is 77 characters, inside the bounty gate of 1–200 characters
of UTF-8 text.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/dad-joke-out python3 main.py
cat /tmp/dad-joke-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
