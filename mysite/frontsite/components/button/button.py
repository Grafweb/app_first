from django_components import Component, register

@register("button")
class Button(Component):
    template_name = "button/button.html"
    
    def get_context_data(self, text, variant="primary"):
        return {
            "text": text,
            "variant": variant,
        }
    
    class Media:
        css = "button/button.css"