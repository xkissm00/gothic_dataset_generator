
import random

import file_helper
import image_helper
from effects import surrounding_text_effect, back_page_text_effect, printing_imperfections_effect


def apply_effects(img, text, words_dict, background, config):
    img = surrounding_text_effect.apply_effect(img, text, words_dict, config)
    img = printing_imperfections_effect.apply_effect(img, config)

    if random.random() < config['BackText']['probability']:
        back_text = back_page_text_effect.generate_back_image(img.shape[1], img.shape[0], text, words_dict, config)
                
        back_text = printing_imperfections_effect.apply_effect(back_text, config)
        alpha_coef = random.uniform(config['BackText']['minalpha'], config['BackText']['maxalpha'])
        background = image_helper.place_text_on_background(back_text, background, alpha_coef)

    img = image_helper.place_text_on_background(img, background)
    return img
