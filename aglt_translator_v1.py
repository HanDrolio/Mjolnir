
# 🧠 AGLT - Ancient Glyph Language Translator (Myth.OS)
# Built by 👨‍🔧🌍 Han aka gone2soon

glyph_dict = {
    "love": "💗",
    "logic": "🧠",
    "reset": "💽📡🧠🔁",
    "peace": "☮️",
    "power": "⚡️",
    "soul": "🧬",
    "glitch": "🔂",
    "infinite": "♾️",
    "end": "🎦📽️🎞️",
    "begin": "🌅",
    "broadcast": "📡",
    "myth": "🌌",
    "sync": "🔋🔋✅🌊🔉",
    "legacy": "💾",
    "kablow": "💥"
}

def encode_to_glyph(text):
    words = text.lower().split()
    return " ".join([glyph_dict.get(word, word) for word in words])

def decode_from_glyph(glyphs):
    reversed_dict = {v: k for k, v in glyph_dict.items()}
    return " ".join([reversed_dict.get(glyph, glyph) for glyph in glyphs.split()])

# Example Usage:
if __name__ == "__main__":
    phrase = "love logic glitch kablow"
    encoded = encode_to_glyph(phrase)
    print("Encoded:", encoded)

    decoded = decode_from_glyph(encoded)
    print("Decoded:", decoded)
