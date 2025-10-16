import emoji

# Lista de emojis disponíveis
print("Emojis disponíveis:")
print("❤️ - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:")

# Solicita a frase codificada
frase = input("\nDigite uma frase e ela será emojizada:\n")

# Converte os códigos de emoji para os emojis reais
frase_emojizada = emoji.emojize(frase, language='alias')

print("\nFrase emojizada:")
print(frase_emojizada)
