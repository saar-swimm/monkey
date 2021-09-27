from typing import Dict, List


def get_config_schema_per_attack_technique(schema: Dict) -> Dict[str, Dict[str, List[str]]]:
    """
    :return: dictionary mapping each attack technique to relevant config fields; example -
            {
                "T1003": {
                    "System Info Collectors": [
                        "Mimikatz collector",
                        "Azure credential collector"
                    ]
                }
            }
    """
    reverse_schema = {}

    definitions = schema["definitions"]
    for definition in definitions:
        definition_type = definitions[definition]["title"]
        for field in definitions[definition]["anyOf"]:
            config_field = field["title"]
            for attack_technique in field.get("attack_techniques", []):
                _add_config_field_to_reverse_schema(
                    definition_type, config_field, attack_technique, reverse_schema
                )

    return reverse_schema


def _add_config_field_to_reverse_schema(
    definition_type: str, config_field: str, attack_technique: str, reverse_schema: Dict
) -> None:
    reverse_schema.setdefault(attack_technique, {})
    reverse_schema[attack_technique].setdefault(definition_type, [])
    reverse_schema[attack_technique][definition_type].append(config_field)
