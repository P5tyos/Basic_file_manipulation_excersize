<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
</head>
<body>
  <h1>File Management and Word Search Program</h1>

  <p>
    This Python program provides a simple command-line interface for managing text files and searching for words within them. It is designed for beginners to practice file handling and string manipulation in Python.
  </p>

  <h2>Features</h2>
  <ul>
    <li><strong>Create and add text to a file</strong><br />
      Append user input and sample text to a new or existing file.
    </li>
    <li><strong>Display file content</strong><br />
      View the contents of a text file with line numbers.
    </li>
    <li><strong>Create a copy of a file</strong><br />
      Duplicate an existing text file with <code>_copy</code> appended to the filename.
    </li>
    <li><strong>Search for a word in a file</strong><br />
      Count how many times an exact word appears in a file (not as part of other words).
    </li>
    <li><strong>Exit the program</strong><br />
      Quit the application safely.
    </li>
  </ul>

  <h2>How to Use</h2>
  <ol>
    <li>Run the Python program.</li>
    <li>You will see a menu with options:
      <ul>
        <li><code>1</code> to create or add text to a file.</li>
        <li><code>2</code> to display the content of a file.</li>
        <li><code>3</code> to create a copy of a file.</li>
        <li><code>4</code> to search a file for a specific word.</li>
        <li><code>m</code> to show the menu again.</li>
        <li><code>x</code> to exit the program.</li>
      </ul>
    </li>
    <li>Follow the prompts to enter filenames and text as needed.</li>
    <li>The program will perform the requested action and return to the menu until you choose to exit.</li>
  </ol>

  <h2>Requirements</h2>
  <p>Python 3.10 or higher</p>

  <h2>Author</h2>
  <p>Greg Horvath<br />
    Date: 2026-04-07
  </p>

  <h2>Example</h2>
  <pre><code>Choose a menu option: 1
Please enter the name of the file you'd like to use: example
Please enter text you'd like to save into the file: Hello world!

Choose a menu option: 2
Please enter the name of the file you'd like to view: example
1: Hello world!
2: This is a python sample text that contains the word python many times, to practice working with files in python.

Choose a menu option: 4
Please enter the name of the file you'd like to search in: example
Please enter the word you'd like to find: python
The word 'python' was found 3 times in the file.
</code></pre>

</body>
</html>
