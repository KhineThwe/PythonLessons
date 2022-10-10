import secrets
print('Printing integer number using secrets module')
passwordresetLink = "https://khine.com//ncc/ncc/reset="
passwordresetLink += secrets.token_urlsafe()#32 bytes ထိသုံးတယ်
print('Generating secure URL',passwordresetLink)
