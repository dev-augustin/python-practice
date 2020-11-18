def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("wide area network")) # Should be: WAN
print(initials("General manager")) # Should be: GM
print(initials("Save our Soul")) # Should be: SOS