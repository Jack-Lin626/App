def replace_words(input_file, output_file, replacements):
    with open(input_file, 'r') as file:
        content = file.read()

    from collections import defaultdict

    word_counts = defaultdict(int)

    # Assuming content is your original text and replacements is your dictionary
    for old_word, new_word in replacements.items():
        word_counts[old_word] = 0  # Initialize word count for each old_word

    lines = content.split('\n')
    new_lines = []

    for line in lines:
        words = line.split()
        new_words = []

        indentation = 0  # Track indentation within the line
        for word_index, word in enumerate(words):
            if word in replacements:
                word_counts[word] += 1
                if word_counts[word] % 2 == 1:  # Replace only if the count is odd
                    words[word_index] = new_word

            # Preserve indentation if word is at the beginning of the line
            if word_index == 0:
                indentation = len(line) - len(line.lstrip())

        new_line = ' ' * indentation + ' '.join(words)
        new_lines.append(new_line)

    new_content = '\n'.join(new_lines)

    with open(output_file, 'w') as file:
        file.write(new_content)

if __name__ == "__main__":
    input_file = 'history.txt'
    output_file = 'historynew.txt'

    # Define your replacements as a dictionary
    # For example: {'old_word1': 'new_word1', 'old_word2': 'new_word2'}
    replacements = {'```': '```cpp='}

    replace_words(input_file, output_file, replacements)

    print(f"Words replaced. Check the '{output_file}' file.")
