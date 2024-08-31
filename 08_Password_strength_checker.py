# Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong)

password=len(input("Enter your password: "))

if password < 6:
    strength="Weak"
elif password <= 10:
    strength="Medium"
else: strength="Strong"

print(f"Password strength is: {strength}")
