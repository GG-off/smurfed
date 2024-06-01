# smurfed ~ easy bulk LMM in Linux CLI

'smurfed' applies system prompt on data with LLM for free bulk generation.

Tested with smurfes (using 'schroumphf' and 'schroumphfer' in the french prompt)

The free GROQ_API_KEY is sourced from environment variable.

This project is an edited clone of 'poked' which is an old ariya's 'ask-llm' fork https://github.com/ariya/ask-llm

It needs Linux Shell + Python version v3.10 or higher (JS GO and CLJ are pretty artefacts for art colors stats and references)

```
git clone https://github.com/GG-off/smurfed/
cd smurfed
chmod +x smurfed.sh
export LLM_API_KEY="[YOUR_OWN_FREE_GROQ_API_KEY]"
./smurfed.sh
```

### to do :
- JSON and CSV input
- free mode for CLI usage (prompt editing, flags, etc.)
- for now it is not random when supposed to be and there's no seed controle yet

read doc for licence and rights questions I guess ; MIT was the one of ariya's ask-llm https://github.com/ariya/ask-llm

NOT related to SMURF trademark or whatever company or holding.
