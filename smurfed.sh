#!/bin/bash
# smurfed.sh
# smurfed applies system prompt on data with LLM for free bulk generation.
# tested with smurfes (schroumphf in french)
# this project is an edited clone of 'poked' which is an old 'ask-llm' fork.
# free GROQ_API_KEY is localy sourced from ~/.aliases

preparation() {
	export LLM_CHAT_MODEL="llama3-70b-8192"
	# export LLM_CHAT_MODEL="llama3-8b-8192"
	# export LLM_CHAT_MODEL="mixtral-8x7b-32768"
	# export LLM_CHAT_MODEL="gemma-7b-it"

	export LLM_TEMPERATURE=1.2 # float 0 to 2
	# export LLM_SEED=100 # problème si j'active ça j'ai aucune valeur pour retourner à void pour que ce soit random

	# export LLM_MAX_TOKENS=32768
	export LLM_MAX_TOKENS=8192

	export LLM_SYSTEM_PROMPT="Je fais de la bande dessinée et tu es un LLM qui m'assiste. Tu reformules en remplaçant des mots par schroumphf et schroumphfer, ainsi qu'en faisant rimer les phrases, sans en faire trop. Tu ajoutes aussi des smileys bucoliques."

	mkdir descriptions
}

ask-llm() {
	file="$1"
	cat "$file"
	cat "$file" | ./../ask-llm.py >> ../answer_"$file"
	sleep 1
}

afficher_reponse() {
	file="$1"
	cat ../answer_"$file"
}

bulk_generation() {
	cd descriptions
	for file in *.txt ; do
		ask-llm "$file"
		afficher_reponse "$file"
	done
}

run() {
	preparation
	echo "y'a rien à faire de plus : let's go!"
	bulk_generation
}

run

exit 0
