"""
Utility class for converting between different naming conventions.
Supports snake_case, PascalCase, camelCase, and kebab-case conversions.
"""

# از این کلاس به عنوان fallback استفاده می‌کنیم در صورت عدم دسترسی به Choices
class FallbackChoices:
    FORMATS = ['API', 'XML', 'JSON', 'HTTP', 'HTTPS', 'URL', 'URI', 'SQL', 'CSS', 'HTML']


try:
    from cinix.base.__serializers__ import Choices
except ImportError:
    Choices = FallbackChoices


class SnakePascalName:
    """
    Utility class for converting between different naming conventions.
    Supports snake_case, PascalCase, camelCase, and kebab-case conversions.
    Includes support for acronyms and various edge cases.
    """

    # Common acronyms that should be kept as uppercase in conversions
    COMMON_ACRONYMS = Choices.FORMATS

    @classmethod
    def to_snake_case(cls, original_name: str) -> str:
        """
        Convert PascalCase or CamelCase to snake_case with acronym support.

        Args:
            original_name: String in PascalCase or CamelCase format

        Returns:
            String converted to snake_case

        Example:
            >>> SnakePascalName.to_snake_case('HelloWorld')
            'hello_world'
            >>> SnakePascalName.to_snake_case('APIEndpoint')
            'api_endpoint'
        """
        if not original_name:
            return ""

        # Handle the case where entire string might be uppercase
        if original_name.isupper():
            return original_name.lower()

        result = []
        prev_char = ''

        for i, char in enumerate(original_name):
            current_char_upper = char.isupper()
            prev_char_lower = prev_char.islower() if prev_char else False

            # Insert underscore when transitioning from lowercase to uppercase
            # or when transitioning from uppercase to lowercase (end of acronym)
            if current_char_upper and prev_char_lower:
                result.append('_')
                result.append(char.lower())
            elif (current_char_upper and prev_char and prev_char.isupper() and i < len(original_name) - 1 and
                  original_name[i + 1].islower()):
                # We're at the last character of an acronym
                result.append('_')
                result.append(char.lower())
            else:
                result.append(char.lower())

            prev_char = char

        return ''.join(result)

    @classmethod
    def to_pascal_case(cls, original_name: str, preserve_acronyms: bool = True) -> str:
        """
        Convert snake_case to PascalCase.

        Args:
            original_name: String in snake_case format
            preserve_acronyms: Whether to preserve common acronyms as uppercase

        Returns:
            String converted to PascalCase

        Example:
            >>> SnakePascalName.to_pascal_case('hello_world')
            'HelloWorld'
            >>> SnakePascalName.to_pascal_case('api_endpoint')
            'ApiEndpoint'
        """
        if not original_name:
            return ""

        parts = original_name.split('_')
        capitalized_parts = []

        for part in parts:
            if preserve_acronyms and part in cls.COMMON_ACRONYMS:
                capitalized_parts.append(part.upper())
            else:
                capitalized_parts.append(part.capitalize())

        return ''.join(capitalized_parts)

    @classmethod
    def to_camel_case(cls, original_name: str, preserve_acronyms: bool = True) -> str:
        """
        Convert snake_case to camelCase.

        Args:
            original_name: String in snake_case format
            preserve_acronyms: Whether to preserve common acronyms as uppercase

        Returns:
            String converted to camelCase

        Example:
            >>> SnakePascalName.to_camel_case('hello_world')
            'helloWorld'
            >>> SnakePascalName.to_camel_case('user_name')
            'userName'
        """
        if not original_name:
            return ""

        parts = original_name.split('_')
        camel_parts = [parts[0]]

        for part in parts[1:]:
            if preserve_acronyms and part in cls.COMMON_ACRONYMS:
                camel_parts.append(part.upper())
            else:
                camel_parts.append(part.capitalize())

        return ''.join(camel_parts)

    @classmethod
    def to_kebab_case(cls, original_name: str) -> str:
        """
        Convert snake_case or PascalCase to kebab-case.

        Args:
            original_name: String in any format

        Returns:
            String converted to kebab-case

        Example:
            >>> SnakePascalName.to_kebab_case('hello_world')
            'hello-world'
            >>> SnakePascalName.to_kebab_case('HelloWorld')
            'hello-world'
        """
        snake = cls.to_snake_case(original_name)
        return snake.replace('_', '-')

    @classmethod
    def detect_case(cls, text: str) -> str:
        """
        Detect the naming convention of the given string.

        Args:
            text: String to analyze

        Returns:
            String indicating the detected case:
            'snake_case', 'PascalCase', 'camelCase', 'kebab-case', or 'unknown'

        Example:
            >>> SnakePascalName.detect_case('hello_world')
            'snake_case'
            >>> SnakePascalName.detect_case('HelloWorld')
            'PascalCase'
        """
        if '_' in text:
            return 'snake_case'
        elif '-' in text:
            return 'kebab-case'
        elif text and text[0].isupper():
            return 'PascalCase'
        elif text and text[0].islower() and any(c.isupper() for c in text[1:]):
            return 'camelCase'
        else:
            return 'unknown'