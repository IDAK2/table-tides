# Table Tides

## Invitation leaf

**Account:** IDAK2  
**Network:** GenLayer StudioNet  
**Category:** Projects  
**Primary tag:** Gaming

**Live site:** https://table-tides.pages.dev/  
**Repository:** https://github.com/IDAK2/table-tides  
**Contract:** `0xfa36Fe492CB4032e0FEeE1B708Ad9013aa58A11B`

## The room promise

A good seating plan is more than capacity arithmetic. Guests need access, requested distance, and enough shared ground for a table to feel alive. Table Tides turns that human arrangement into a cooperative on-chain puzzle without asking one host to be the sole judge.

## Place-card law

The host freezes an occasion, guest profiles, table capacities, and explicit constraints. Each participating wallet can propose only one placement. Code rejects reused guests, occupied chairs, invalid table indexes, and over-capacity seats before consensus begins.

## Jury etiquette

Validators independently judge one exact placement against the frozen access and separation rules, then check conversational balance without inventing guest facts. A rejected proposal spends one conflict allowance. A full room becomes `SEATED`; an exhausted allowance becomes `PAUSED` instead of trapping the dinner permanently.

## Host preparation

```text
cd frontend
npm install
npm run typecheck
npm run build
```

Run contract surface checks with `pytest tests -q`. The exported frontend reads the live room and sends placement transactions through a connected StudioNet wallet.

## Chain record

`deployment.json` carries the verified address, deployment transaction, lifecycle transaction, public room key, repository, and Cloudflare URL.

## Last course

This is an inclusive planning game, not a profiling or eligibility system. Real hosts should confirm access needs directly and avoid storing sensitive personal information on a public chain.
