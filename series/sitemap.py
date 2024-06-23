from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
from xml.dom import minidom

def generate_sitemap(urls, output_file):
    urlset = Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')

    for url in urls:
        url_element = SubElement(urlset, 'url')
        loc = SubElement(url_element, 'loc')
        loc.text = url

    # Convert the ElementTree to a byte string
    rough_string = tostring(urlset, 'utf-8')

    # Pretty print the XML
    reparsed = minidom.parseString(rough_string)
    pretty_xml_as_string = reparsed.toprettyxml(indent="  ")

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(pretty_xml_as_string)

def main():
    urls = [
        "https://dashflix.top/movies/3%20Body%20Problem.html",
        "https://dashflix.top/movies/Arcane.html",
        "https://dashflix.top/movies/Attack%20on%20Titan.html",
        "https://dashflix.top/movies/Avatar%20The%20Last%20Airbender%202005.html",
        "https://dashflix.top/movies/Avatar-The-Last-Airbender.html",
        "https://dashflix.top/movies/Band%20of%20Brothers.html",
        "https://dashflix.top/movies/Batman%20The%20Animated%20Series.html",
        "https://dashflix.top/movies/Beacon%2023.html",
        "https://dashflix.top/movies/Better%20Call%20Saul.html",
        "https://dashflix.top/movies/Black%20Mirror.html",
        "https://dashflix.top/movies/Breaking%20Bad.html",
        "https://dashflix.top/movies/Brooklyn%20Nine-Nine.html",
        "https://dashflix.top/movies/Cobra%20Kai.html",
        "https://dashflix.top/movies/Cowboy%20Bebop.html",
        "https://dashflix.top/movies/Daredevil.html",
        "https://dashflix.top/movies/Dark%20Matter.html",
        "https://dashflix.top/movies/Dark.html",
        "https://dashflix.top/movies/Dexter.html",
        "https://dashflix.top/movies/Downton%20Abbey.html",
        "https://dashflix.top/movies/Echo.html",
        "https://dashflix.top/movies/Eric.html",
        "https://dashflix.top/movies/Euphoria.html",
        "https://dashflix.top/movies/Fallout.html",
        "https://dashflix.top/movies/Friends.html",
        "https://dashflix.top/movies/From.html",
        "https://dashflix.top/movies/Fullmetal%20Alchemist%20Brotherhood.html",
        "https://dashflix.top/movies/Game%20of%20Thrones.html",
        "https://dashflix.top/movies/Geek%20Girl.html",
        "https://dashflix.top/movies/Grimm.html",
        "https://dashflix.top/movies/Halo.html",
        "https://dashflix.top/movies/Hierarchy.html",
        "https://dashflix.top/movies/How%20I%20Met%20Your%20Mother.html",
        "https://dashflix.top/movies/Invincible.html",
        "https://dashflix.top/movies/Jurassic%20World%20Chaos%20Theory.html",
        "https://dashflix.top/movies/Knuckles.html",
        "https://dashflix.top/movies/Lost.html",
        "https://dashflix.top/movies/Lucifer.html",
        "https://dashflix.top/movies/Mad%20Men.html",
        "https://dashflix.top/movies/Masters%20of%20the%20Air.html",
        "https://dashflix.top/movies/Maxton%20Hall%20The%20World%20Between%20Us.html",
        "https://dashflix.top/movies/Mayor%20of%20Kingstown.html",
        "https://dashflix.top/movies/Modern%20Family.html",
        "https://dashflix.top/movies/Monarch%20Legacy%20of%20Monsters.html",
        "https://dashflix.top/movies/Mr%20and%20Mrs%20Smith.html",
        "https://dashflix.top/series/One%20Piece.html",
        "https://dashflix.top/movies/Parasyte%20The%20Grey.html",
        "https://dashflix.top/movies/Peacemaker.html",
        "https://dashflix.top/movies/Peaky%20Blinders.html",
        "https://dashflix.top/movies/Percy%20Jackson%20and%20the%20Olympians.html",
        "https://dashflix.top/movies/Presumed%20Innocent.html",
        "https://dashflix.top/movies/Prison%20Break.html",
        "https://dashflix.top/movies/Raising%20Voices.html",
        "https://dashflix.top/series/One%20Piece.html",
        "https://dashflix.top/movies/Reacher.html",
        "https://dashflix.top/movies/Rick%20and%20Morty.html",
        "https://dashflix.top/movies/Severance.html",
        "https://dashflix.top/movies/Shameless.html",
        "https://dashflix.top/movies/Sherlock.html",
        "https://dashflix.top/movies/Shogun.html",
        "https://dashflix.top/movies/Smallville.html",
        "https://dashflix.top/movies/Solo-Leveling.html",
        "https://dashflix.top/movies/Squid%20Game.html",
        "https://dashflix.top/movies/Star%20Trek%20Discovery.html",
        "https://dashflix.top/movies/Stranger%20Things.html",
        "https://dashflix.top/movies/Succession.html",
        "https://dashflix.top/movies/Suits.html",
        "https://dashflix.top/movies/Supernatural.html",
        "https://dashflix.top/movies/Ted%20Lasso.html",
        "https://dashflix.top/movies/Ted.html",
        "https://dashflix.top/movies/The%20Big%20Bang%20Theory.html",
        "https://dashflix.top/movies/The%20Boys.html",
        "https://dashflix.top/movies/The%20Last%20of%20Us.html",
        "https://dashflix.top/movies/The%20Lord%20of%20the%20Rings%20The%20Rings%20of%20Power.html",
        "https://dashflix.top/movies/The%20Mandalorian.html",
        "https://dashflix.top/movies/The%20Office.html",
        "https://dashflix.top/movies/The%20Punisher.html",
        "https://dashflix.top/movies/The%20Sopranos.html",
        "https://dashflix.top/movies/The%20Sympathizer.html",
        "https://dashflix.top/movies/The%20Umbrella%20Academy.html",
        "https://dashflix.top/movies/The%20Vampire%20Diaries.html",
        "https://dashflix.top/movies/The%20Veil.html",
        "https://dashflix.top/movies/The-Walking-Dead-The-Ones-Who-Live.html",
        "https://dashflix.top/movies/The%20Walking%20Dead.html",
        "https://dashflix.top/movies/The%20Wire.html",
        "https://dashflix.top/movies/Titans.html",
        "https://dashflix.top/movies/Tracker.html",
        "https://dashflix.top/movies/Under%20the%20Bridge.html",
        "https://dashflix.top/movies/Vikings.html",
        "https://dashflix.top/movies/Wednesday.html",
        "https://dashflix.top/movies/Westworld.html",
        "https://dashflix.top/movies/X-Men%2097.html",
        "https://dashflix.top/movies/Young%20Justice.html",
        "https://dashflix.top/movies/Young%20Sheldon.html",
        "https://dashflix.top/movies/Yu%20Yu%20Hakusho.html"

    ]
    output_file = 'sitemap.xml'

    generate_sitemap(urls, output_file)
    print(f"Sitemap generated and saved to {output_file}")

if __name__ == "__main__":
    main()
