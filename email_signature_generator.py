import pandas as pd
import os

# Read the Excel file
df = pd.read_excel('user_list.xlsx')

# Create the 'Signatures' folder if it doesn't exist
if not os.path.exists('Signatures'):
    os.makedirs('Signatures')

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    firstName = row['name'].upper()
    lastName = row['surname'].upper()
    role = row['role']
    mail = row['mail']
    phone = row['phone']

    # Create the HTML code for the signature
    html = f"""<table style="border-collapse: separate;table-layout: fixed;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;max-width:350px;" emb-background-style="">
                 <tbody>
                 <tr>
                   <td style="color:#555555;font-size:13px;height:118px;padding-bottom:15px;font-family:Trebuchet MS, Verdana, Verdana Ref, sans-serif;">
                     <p style="margin:.1px;">
                       <a href="#" style="border:0;display:block;height:118px;" target="_blank">
                         <img src="YOUR LOGO URL" width="265" height="118" style="display:block;border:0;" nosend="1" alt="">
                       </a>
                     </p>
                   </td>
                 </tr>
                 <tr>
                   <td style="color:#555555;font-size:13px;mso-line-height-rule:exactly;line-height:24px;font-family:Trebuchet MS, Verdana, Verdana Ref, sans-serif;">
                     <p style="margin:.1px;">
                       <span style="font-weight:bold;color:#333333;font-size:16px;letter-spacing:2px;">{firstName} {lastName}</span>
                       <span style="letter-spacing:2px;"> |  {role}</span>
                     </p>
                   </td>
                 </tr>
                 <tr>
                   <td style="color:#555555;font-size:13px;mso-line-height-rule:exactly;line-height:20px;font-family:Trebuchet MS, Verdana, Verdana Ref, sans-serif;">
                     <p style="margin:.1px;">Email:
                       <a href="mailto:{mail}" style="color:#333333;text-decoration:none;" target="_blank">{mail}</a>
                     </p>
                   </td>
                 </tr>
                 <tr>
                   <td style="color:#555555;font-size:13px;mso-line-height-rule:exactly;line-height:20px;font-family:Trebuchet MS, Verdana, Verdana Ref, sans-serif;">
                     <p style="margin:.1px;">Mob:
                       <a href="tel:00{phone}" style="color:#333333;text-decoration:none;" target="_blank">+{phone}</a>
                     </p>
                   </td>
                 </tr>
                 <tr>
                   <td style="color:#555555;font-size:13px;mso-line-height-rule:exactly;line-height:20px;font-family:Trebuchet MS, Verdana, Verdana Ref, sans-serif;">
                     <p style="margin:.1px;">
                       <a href="#" style="color:#333333;text-decoration:none;" target="_blank">YOUR ADDRESS</a>
                     </p>
                   </td>
                 </tr>
                 <tr>
                   <td style="color:#555555;font-size:13px;mso-line-height-rule:exactly;line-height:20px;font-family:Trebuchet MS, Verdana, Verdana Ref, sans-serif;">
                     <p style="margin:.1px;">
                       <span style="font-weight:bold;letter-spacing:2px;">
                         <a href="#" style="color:#333333;text-decoration:none;" target="_blank">DOMAIN.COM</a>
                       </span>
                     </p>
                   </td>
                 </tr>
                 </tbody>
               </table>"""
    
    # Create an HTML file for the signature
    with open(f'Signatures/{firstName} {lastName} ({mail}).htm', 'w') as file:
        file.write(html)