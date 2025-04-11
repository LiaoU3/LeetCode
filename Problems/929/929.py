class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # Remove all the . from the local name
        # Combine the local name and domain name back together
        mails = set()
        for email in emails:
            local = email.split("@")[0].split("+")[0]
            new_local = ""
            for c in local:
                if c.isalpha():
                    new_local += c
            new_email = new_local + "@" + email.split("@")[1]
            # Add the email to a set
            mails.add(new_email)
        # Return the length of the set
        return len(mails)
