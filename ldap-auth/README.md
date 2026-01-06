# LDAP Authentication

## Problem Description
Implement a user authentication system using LDAP (Lightweight Directory Access Protocol) to validate user credentials against a directory server.

## Background
LDAP is a widely-used protocol for accessing and maintaining distributed directory information services over a network. It's commonly used in enterprise environments for centralized authentication, allowing users to log in with a single set of credentials across multiple applications.

## Objectives
Build an application that:
1. Connects to an LDAP server
2. Authenticates users by validating their username and password
3. Retrieves user information from the directory after successful authentication
4. Handles authentication failures gracefully
5. Implements proper connection management and error handling

## Requirements

### Core Functionality
- **LDAP Connection**: Establish a secure connection to an LDAP server
- **User Authentication**: Bind to the LDAP server using provided credentials
- **User Search**: Query the directory to find user entries
- **Attribute Retrieval**: Fetch user attributes (e.g., displayName, email, groups)
- **Error Handling**: Handle common scenarios:
  - Invalid credentials
  - Connection failures
  - User not found
  - Server unavailable

### Configuration Parameters
Your solution should support configurable:
- LDAP server URL (e.g., `ldap://localhost:389` or `ldaps://server:636`)
- Base DN (Distinguished Name) for user searches
- Bind DN template or admin credentials
- Search filter (e.g., `(uid={username})` or `(sAMAccountName={username})`)
- Connection timeout settings

### Security Considerations
- Use LDAPS (LDAP over SSL/TLS) when possible
- Avoid logging sensitive information (passwords)
- Properly close connections after use
- Sanitize user input to prevent LDAP injection

## Test Scenarios

### Scenario 1: Successful Authentication
**Input:**
- Username: `jdoe`
- Password: `correct_password`

**Expected Output:**
- Authentication successful
- User details retrieved:
  - Display Name: John Doe
  - Email: jdoe@example.com
  - Groups: [developers, users]

### Scenario 2: Invalid Credentials
**Input:**
- Username: `jdoe`
- Password: `wrong_password`

**Expected Output:**
- Authentication failed
- Error message: "Invalid credentials"

### Scenario 3: User Not Found
**Input:**
- Username: `nonexistent`
- Password: `any_password`

**Expected Output:**
- Authentication failed
- Error message: "User not found"

### Scenario 4: Connection Failure
**Input:**
- Invalid LDAP server URL

**Expected Output:**
- Connection error
- Error message: "Unable to connect to LDAP server"

## Implementation Notes

### Setting Up a Test LDAP Server
For testing purposes, you can use:
- **Docker**: Run OpenLDAP container
  ```powershell
  docker run -p 389:389 -p 636:636 --name test-ldap osixia/openldap:latest
  ```
- **Online LDAP Test Server**: Use public test servers (for learning only)
- **Local Directory**: Active Directory (Windows) or OpenLDAP (Linux)

### Common LDAP Attributes
- `cn` (Common Name): Full name
- `uid` or `sAMAccountName`: Username
- `mail`: Email address
- `memberOf`: Group memberships
- `telephoneNumber`: Phone number
- `title`: Job title

## Bonus Challenges
1. Implement connection pooling for better performance
2. Add support for LDAP group-based authorization
3. Implement password change functionality
4. Add caching for user lookups to reduce server load
5. Create a simple web interface for testing authentication
6. Support multiple LDAP servers with failover
7. Implement user session management after successful authentication

## Example Usage
```
# Authenticate user
authenticate("jdoe", "password123")

# Get user details
user = get_user_info("jdoe")
print(user.display_name)  # Output: John Doe
print(user.email)         # Output: jdoe@example.com

# Check group membership
is_admin = user.is_member_of("administrators")
```

## Resources
- LDAP Protocol: RFC 4511
- LDAP Authentication Best Practices
- Common LDAP libraries by language:
  - Python: `python-ldap`, `ldap3`
  - JavaScript: `ldapjs`
  - Java: `UnboundID LDAP SDK`
  - C#: `System.DirectoryServices`