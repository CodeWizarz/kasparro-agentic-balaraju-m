class TemplateAgent:
    def apply_template(self, template: dict, blocks: dict) -> dict:
        page = {
            "page_type": template["page_type"],
            "sections": {}
        }

        # Validate required blocks
        for block in template["required_blocks"]:
            if block not in blocks:
                raise ValueError(f"Missing required block: {block}")

        # Assemble sections
        for section in template["layout"]:
            block_name = section["block"]
            page["sections"][section["section_id"]] = blocks[block_name]

        return page
