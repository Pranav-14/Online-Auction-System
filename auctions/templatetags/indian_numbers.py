from django import template

register = template.Library()


@register.filter(name="format_inr")
def format_inr(value):
    """
    Formats a number or numeric string into Indian Rupee currency format (₹ X,XX,XXX).
    Examples:
        1500 -> ₹ 1,500
        150000 -> ₹ 1,50,000
        10000000 -> ₹ 1,00,00,000
        150000.50 -> ₹ 1,50,000.50
    """
    if value is None or value == "":
        return "₹ 0"

    try:
        val_str = str(value).strip()
        is_negative = False
        if val_str.startswith("-"):
            is_negative = True
            val_str = val_str[1:]

        if "." in val_str:
            parts = val_str.split(".", 1)
            int_part, dec_part = parts[0], parts[1]
            if dec_part == "0" or dec_part == "00":
                dec_str = ""
            else:
                dec_str = f".{dec_part[:2]}"
        else:
            int_part = val_str
            dec_str = ""

        int_part = "".join(filter(str.isdigit, int_part))
        if not int_part:
            return "₹ 0"

        if len(int_part) <= 3:
            formatted_int = int_part
        else:
            last_three = int_part[-3:]
            rest = int_part[:-3]
            groups = []
            while len(rest) > 2:
                groups.insert(0, rest[-2:])
                rest = rest[:-2]
            if rest:
                groups.insert(0, rest)
            formatted_int = ",".join(groups) + "," + last_three

        prefix = "-₹ " if is_negative else "₹ "
        return f"{prefix}{formatted_int}{dec_str}"
    except (ValueError, TypeError):
        return f"₹ {value}"
