# Email Signature Generator

This Python script generates HTML email signatures for each user in an Excel file.

## Prerequisites

The script requires the following Python libraries:

- pandas
- openpyxl
- os

You can install these libraries using pip:

```bash
pip install pandas
pip install openpyxl
```

## Usage

1. First, you will need to populate the `user_list.xlsx` file with your users' details. Ensure that the Excel file has columns in the following order:
    - name
    - surname
    - role
    - mail
    - phone

2. Next, you'll need to customize the HTML signature present in the Python script itself. Be sure to replace the placeholder texts like 'YOUR LOGO URL', 'YOUR ADDRESS', and 'DOMAIN.COM' with your actual organization's respective details.

3. Run the script. This will generate an HTML file for each user in a directory named 'Signatures'. If this directory does not already exist, the script will create it.

To run the script, use the following command:

```bash
python email_signature_generator.py
```

## File Naming Convention

The Python script generates HTML files for each user's signature, following a specific naming format: `FIRSTNAME LASTNAME (email).htm`. As an example, consider a user named `John Doe` with the email address `john.doe@example.com`. For this user, the script will create an HTML file named `JOHN DOE (john.doe@example.com).htm`.

## Customizing the HTML Template

You're free to modify the HTML template in the Python script as needed to match your organization's signature design standards. The critical aspect is to ensure that you correctly use the variables `{firstName}`, `{lastName}`, `{role}`, `{mail}`, and `{phone}` in the appropriate places within the HTML code. These variables get replaced with actual user data during the execution of the script.

## Important Considerations

- Ensure that the `user_list.xlsx` file is located in the same directory as the Python script before execution. The script reads user information from this file.

- The script generates signatures as basic HTML files. If the intended email client doesn't support HTML signatures, these files might not function as expected.

- Always examine the generated signature files prior to their usage. The script does not perform any validation checks on the input provided in the Excel file. It's crucial to verify the accuracy and appropriateness of the input data.
