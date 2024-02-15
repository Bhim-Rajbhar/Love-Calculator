# Love-Calculator

This code is a simple "Love Calculator" that calculates a "love score" based on two names provided by the user and then provides a message based on the calculated score. Here's a breakdown of how the code works:

The program starts by printing an introductory message: "The Love calculator is calculating your score..."

The user is prompted to input their first full name and their partner's full name using the input() function. The names are stored in variables Name1 and Name2, respectively.

The two names are combined into a single string (Combined_Name) and converted to lowercase (lower_names). This is done to make the comparison case-insensitive.

The code then counts the occurrences of specific letters ('t', 'r', 'u', 'e') in the combined lowercase name. These letters are chosen because they spell "true," representing the first part of the love score calculation. The counts are stored in variables t, r, u, and e, respectively.

Similarly, the code counts the occurrences of specific letters ('l', 'o', 'v', 'e') in the combined lowercase name. These letters are chosen because they spell "love," representing the second part of the love score calculation. The counts are stored in variables l, o, v, and e, respectively.

The first and second parts of the love score are calculated by adding up the counts of the respective letters: first_digit for 'true' and second_digit for 'love'.

The two parts of the love score are concatenated to form a two-digit number (score). This is done by converting the counts to strings, concatenating them, and then converting the result back to an integer.

Based on the calculated score, the code provides different messages:

If the score is less than 10 or greater than 90, it prints "Your score is [score], you go together like coke & mentos."
If the score is between 40 and 50 (inclusive), it prints "Your score is [score], you are alright together."
Otherwise, it prints "Your score is [score]."
The program ends after printing the appropriate message based on the calculated love score.

Overall, this code offers a fun and light-hearted way to generate a "love score" based on inputted names.
