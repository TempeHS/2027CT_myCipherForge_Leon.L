"""
CipherForge — Encryption Engine
================================
Author: [Your Name]
Date: 2026

This file contains my custom 5-layer encryption algorithm.

PHASES:
  1. Substitution — Replace characters with different ones
  2. Transposition — Rearrange the order of characters
  3. Key-Dependent — Make output depend on a secret password
  4. Noise Injection — Add fake characters to confuse attackers
  5. Wild Card — My unique invention!

RULES:
  - encrypt() MUST be reversible
  - decrypt(encrypt(message)) MUST return the original message
"""

# Your encryption code will go below this line!

ord("A")  # Returns: 65
ord("Z")  # Returns: 90
ord("a")  # Returns: 97
ord(" ")  # Returns: 32 (space)
ord("!")  # Returns: 33

chr(65)  # Returns: 'A'
chr(90)  # Returns: 'Z'
chr(97)  # Returns: 'a'
chr(32)  # Returns: ' ' (space)
chr(33)  # Returns: '!'

# Shift a character by 'shift' positions, wrapping around
position = ord(chr) - 32  # Convert to 0-94 range
new_position = (position + shift) % 95  # Add shift, wrap with modulo
result = chr(new_position + 32)  # Convert back to ASCII


def encrypt_message(text, shift):
    """
    Shift every character in the text by a given amount.

    Args:
        text: The message to encrypt (string)
        shift: How many positions to move each character (int)

    Returns:
        The encrypted message (string)
    """


def function_name(param1, param2):
    """
    Brief description of what the function does.

    Args:
        param1: Description of first parameter
        param2: Description of second parameter

    Returns:
        Description of what is returned
    """


def simple_shift(text, shift):
    """
    Shift every character by 'shift' positions.

    This is a simple Caesar cipher that works on ALL printable characters,
    not just letters. It wraps around using modular arithmetic.

    Args:
        text: The string to encrypt
        shift: How many positions to shift (positive = forward)

    Returns:
        The encrypted string
    """
    result = ""

    for char in text:
        if 32 <= ord(char) <= 126:  # Printable ASCII range
            # Convert to 0-94 range
            position = ord(char) - 32
            # Shift and wrap
            new_position = (position + shift) % 95
            # Convert back to character
            result += char(new_position + 32)
        else:
            # Keep non-printable characters unchanged
            result += char

    return result


def simple_unshift(text, shift):
    """
    Reverse the simple_shift encryption.

    Decryption is just shifting in the opposite direction!

    Args:
        text: The encrypted string
        shift: The same shift value used for encryption

    Returns:
        The decrypted (original) string
    """
    # Decryption = shifting backwards (negative)
    return simple_shift(text, -shift)
