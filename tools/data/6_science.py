"""Class 6 Science — all chapters of the NCERT/CBSE book."""

from tools.model import C, E, M, S, T, SUBJECT

SUBJECT_DATA = SUBJECT(
    "6-science", "Science", 6, "NCERT / CBSE Class 6 Science",
    "Class 6 science begins with the world you can see, touch and taste: the food you eat, the "
    "clothes you wear, the materials around you, the plants and animals you share the planet with, "
    "and the simple machines and magnets you play with. Every chapter below has a plain-language "
    "summary, worked examples and practice questions.",
    [
        C(1, "Food: Where Does It Come From?", [
            T("Food Variety and Its Sources",
              "Every living thing needs food. Humans eat a huge variety of food because we are omnivores, "
              "and almost all of it comes either from plants or from animals.",
              ["Plants give us cereals, pulses, fruits, vegetables, spices, oil and sugar.",
               "Animals give us milk, eggs, meat, honey and fish.",
               "Different plant parts are edible: roots (carrot), stems (sugarcane), leaves (spinach), "
               "flowers (broccoli), fruits (tomato) and seeds (rice, wheat).",
               "A food ingredient is what a dish is made from; many dishes combine plant and animal ingredients."],
              [E("A simple meal, traced back",
                 "Rice, dal and milk: rice comes from the seeds of the rice plant, dal from split pulses "
                 "(seeds of legumes), and milk from a cow or buffalo. A vegetarian meal still has two plant "
                 "sources and one animal source."),
               E("Sprouts — a living food",
                 "Soak gram seeds overnight, drain the water and leave them wrapped in cloth for a day. "
                 "Small white shoots appear: the seeds have germinated into sprouts, which are easier to "
                 "digest and richer in some vitamins than dry seeds.")],
              [M("Which of these is an animal product?",
                 "Honey|Rice|Spinach|Mustard oil", 0,
                 "Honey is made by honeybees, so it is an animal product. Rice, spinach and mustard oil are plant products."),
               M("Which plant part do we eat when we eat a carrot?",
                 "Root|Stem|Leaf|Flower", 0,
                 "A carrot is a modified tap root that stores food."),
               S("Name three food items that come from plants and three that come from animals.",
                 "Plants: rice, spinach, mango. Animals: milk, eggs, honey.",
                 "Cereals, pulses, fruits and vegetables are plant foods; milk, egg, meat, fish and honey are animal foods.")]),
            T("What Do Animals Eat?",
              "Animals are grouped by what they eat: herbivores eat plants, carnivores eat other animals, "
              "and omnivores eat both. Some animals also eat dead matter and are called scavengers.",
              ["Herbivores: cow, goat, deer, elephant, rabbit.",
               "Carnivores: lion, tiger, fox, wolf; some eat insects (insectivores) such as the frog and lizard.",
               "Omnivores: human, bear, crow, dog, cockroach.",
               "Scavengers such as vultures and crows eat dead animals and help keep the environment clean.",
               "Parasites such as ticks and lice live on other animals and feed on them."],
              [E("Tiger versus cow",
                 "A tiger has sharp, pointed canine teeth and a short gut — adaptations for tearing and "
                 "digesting meat quickly. A cow has flat grinding teeth and a long gut for breaking down "
                 "plant fibre. Teeth and body design match diet."),
               E("The bee and the flower",
                 "Honeybees visit flowers for nectar and pollen, and in doing so carry pollen from flower to "
                 "flower. The bee gets food and the plant gets pollinated: a partnership, not theft.")],
              [M("A cow is a ______.", "Herbivore|Carnivore|Omnivore|Scavenger", 0,
                 "Cows eat grass and other plant material, so they are herbivores."),
               M("Vultures that eat dead animals are best described as:",
                 "Scavengers|Parasites|Herbivores|Producers", 0,
                 "Animals that feed on dead and decaying matter are scavengers."),
               S("Why does a tiger have sharp, pointed teeth while a cow has flat teeth?",
                 "Teeth are adapted to diet: tigers tear meat with pointed canines, cows grind plant material with flat molars.")]),
        ]),
        C(2, "Components of Food", [
            T("Nutrients in Food",
              "Food contains nutrients — carbohydrates, proteins, fats, vitamins, minerals, water and "
              "roughage — each with a specific job in the body.",
              ["Carbohydrates and fats are energy-giving foods.",
               "Proteins are body-building foods; they are needed for growth and repair.",
               "Vitamins and minerals are protective foods; they keep the body healthy and fight disease.",
               "Water carries nutrients and removes wastes; roughage (dietary fibre) helps the gut push food along.",
               "A simple test for starch uses iodine (blue-black colour); for protein, copper sulphate and "
               "caustic soda give a violet colour; for fat, a translucent oily patch appears on paper."],
              [E("Testing a potato for starch",
                 "Put a drop of dilute iodine on a cut potato. It turns blue-black, showing starch is present. "
                 "Iodine also turns rice water blue-black, but not on a slice of cucumber."),
               E("Why growing children need dal and eggs",
                 "Pulses, milk, eggs, fish and soyabean are rich in protein. Growing children need extra "
                 "protein because new cells are being built every day; a protein-poor diet slows growth.")],
              [M("Which nutrient is the main source of energy?", "Carbohydrate|Protein|Vitamin C|Iron", 0,
                 "Carbohydrates are the body's main fuel and are found in cereals, potato and sugar."),
               M("Iodine solution is used to test for:", "Starch|Protein|Fat|Vitamin", 0,
                 "Iodine turns blue-black in the presence of starch."),
               S("Name the two groups of foods that protect the body from disease.",
                 "Vitamins and minerals.",
                 "Vitamins and minerals are protective nutrients; deficiency causes specific diseases.")]),
            T("Balanced Diet and Deficiency Diseases",
              "A balanced diet contains all nutrients in the right amounts, plus water and roughage. "
              "Missing a nutrient for a long time causes a deficiency disease.",
              ["Deficiency of vitamin A causes night blindness; vitamin B1 causes beriberi; vitamin C causes scurvy; "
               "vitamin D causes rickets; vitamin K affects clotting.",
               "Iron deficiency causes anaemia; iodine deficiency causes goitre; calcium and phosphorus "
               "deficiency weakens bones and teeth.",
               "Protein-energy malnutrition appears as kwashiorkor (swollen belly and legs) and marasmus (extreme thinness).",
               "Cooking can destroy vitamin C; boiling vegetables for long removes water-soluble vitamins, "
               "so steaming or quick cooking is better."],
              [E("A sailor's diet and scurvy",
                 "Sailors on long voyages once ate only dry biscuits and salted meat, and developed bleeding "
                 "gums and loose teeth — scurvy, caused by lack of vitamin C. Adding lemons and oranges cured "
                 "them, which is why citrus fruit was carried on ships."),
               E("Planning a balanced lunch",
                 "Chapati (carbohydrate), dal (protein), a green vegetable (vitamins and minerals), a little "
                 "ghee (fat), a salad (roughage) and a glass of water make a balanced lunch. Only rice and "
                 "ghee would be energy-rich but nutrient-poor.")],
              [M("Night blindness is caused by the deficiency of:", "Vitamin A|Vitamin C|Iron|Calcium", 0,
                 "Vitamin A is needed by the retina; carrots, papaya, mango and green leafy vegetables are good sources."),
               M("Goitre is caused by the deficiency of:", "Iodine|Iron|Vitamin K|Protein", 0,
                 "Iodine is needed to make thyroid hormones; iodised salt prevents goitre."),
               S("What is a balanced diet?", "A diet with all nutrients, water and roughage in the right amounts.",
                 "It supplies energy, building material and protective nutrients in correct proportions, keeping the body healthy.")]),
        ]),
        C(3, "Fibre to Fabric", [
            T("Plant Fibres: Cotton and Jute",
              "Clothes are made from fibres. Natural fibres come from plants (cotton, jute, linen) or "
              "animals (wool, silk); synthetic fibres are made by humans.",
              ["Cotton comes from the bolls of the cotton plant and grows best in black soil and warm climates.",
               "Jute comes from the stem of the jute plant and is harvested when the plant is flowering; "
               "it is called the golden fibre.",
               "Fibres are spun into yarn and yarn is woven or knitted into fabric.",
               "Ginning separates cotton fibres from seeds; retting softens jute stems in water so fibres can be peeled."],
              [E("From field to shirt",
                 "Cotton is picked, ginned, combed and spun into yarn, then woven into cloth and stitched into "
                 "a shirt. Each step removes impurities and lines the fibres up so they can twist into a strong yarn."),
               E("Why jute is used for sacks",
                 "Jute fibres are long, coarse and strong but not very fine, so they make excellent ropes, "
                 "gunny bags and carpets rather than soft clothing.")],
              [M("Jute fibre is obtained from the:", "Stem|Seed|Leaf|Root", 0,
                 "Jute is a bast fibre taken from the stem of the plant."),
               M("The process of separating cotton fibres from seeds is called:", "Ginning|Spinning|Weaving|Retting", 0,
                 "Ginning separates seeds from cotton fibre."),
               S("Write the steps from fibre to fabric.", "Spinning converts fibre to yarn; weaving or knitting converts yarn to fabric.",
                 "Fibres are cleaned, spun into yarn on a spinning wheel or machine, then interlaced (woven) or looped (knitted) into fabric.")]),
            T("Animal Fibres: Wool and Silk",
              "Wool comes from the fleece of sheep and other animals; silk comes from the cocoon of the "
              "silkworm. Both are animal fibres with different properties and processing.",
              ["Sheep are sheared in summer; the fleece is cleaned (scouring), sorted and spun into wool yarn.",
               "The outer hair of sheep is coarse; the under-hair (undercoat) is soft and is used for fine wool.",
               "Silk is produced by the larva of the silkworm moth, which spins a cocoon of silk fibre.",
               "Sericulture is the rearing of silkworms; silk is strong, lustrous and absorbs moisture."],
              [E("Why wool keeps us warm",
                 "Wool fibres trap air between them; air is a poor conductor of heat, so body heat cannot escape "
                 "easily. That is why woollen clothes are used in winter and loosely woven cotton in summer."),
               E("Silk: a protein thread",
                 "A silkworm can spin a continuous filament hundreds of metres long. The filaments from several "
                 "cocoons are twisted together to make a silk thread strong enough for weaving.")],
              [M("Which animal gives us wool?", "Sheep|Silkworm|Cow|Hen", 0, "Sheep fleece is the most common source of wool."),
               M("Sericulture is the rearing of:", "Silkworms|Sheep|Bees|Fish", 0,
                 "Sericulture is silk farming."),
               S("Why is wool a good insulator?", "Its crimped fibres trap air, and trapped air slows heat loss.",
                 "Air trapped between wool fibres is a poor conductor, so it reduces heat transfer from the body.")]),
        ]),
        C(4, "Sorting Materials into Groups", [
            T("Properties of Materials",
              "We group materials by observable properties such as appearance, hardness, solubility, "
              "transparency and conductivity. Grouping makes it easy to study and use materials.",
              ["Materials may be shiny (metals) or dull (wood, rubber, paper).",
               "Hard materials scratch softer ones; iron is harder than chalk, diamond is the hardest natural material.",
               "Some solids dissolve in water (sugar, salt) and are soluble; others (sand, chalk) are insoluble.",
               "Transparent materials let light pass fully (glass), translucent let some light pass (butter paper), "
               "opaque let no light pass (wood).",
               "Metals are good conductors of heat and electricity; wood, plastic, rubber and glass are poor conductors."],
              [E("Sorting a kitchen drawer",
                 "A spoon is shiny, hard, insoluble and opaque. A plastic lid is dull, flexible, insoluble and "
                 "opaque. A glass tumbler is transparent. Sorting by these five properties tells us which item "
                 "suits which job — metal for the pan, plastic for the handle."),
               E("Sugar in cold water versus hot water",
                 "The same spoon of sugar dissolves faster in hot water because heat speeds up the movement of "
                 "water molecules. Solubility is a property of the material, but dissolving speed changes with temperature.")],
              [M("Which material is transparent?", "Glass|Wood|Cardboard|Iron", 0, "Glass allows most light to pass through."),
               M("Materials that do not allow electricity to pass are called:", "Insulators|Conductors|Solutes|Soluble", 0,
                 "Insulators such as rubber and plastic resist the flow of current."),
               S("Name three properties used to sort materials.", "Appearance, hardness and solubility (also transparency and conductivity).")]),
            T("Why Grouping Matters",
              "Sorting is not just neatness: grouping reveals patterns, helps us choose the right material "
              "for a purpose and is the first step of scientific classification.",
              ["Objects made of the same material share properties even when their shape differs.",
               "Grouping lets us predict behaviour: all metals conduct, all plastics insulate.",
               "Mixing materials can change properties — glass is transparent but brittle, so safety glass is layered.",
               "Early scientists grouped living things and substances; modern chemistry uses the same logic with elements and compounds."],
              [E("Cooking utensils",
                 "The body of a pan is metal because metals conduct heat well. The handle is plastic or wood "
                 "because those materials do not conduct heat, so they protect our hands. Two material groups, one object."),
               E("Recycled sorting",
                 "A recycling centre separates paper, plastic, glass and metal by hand and by machine. Each "
                 "group is processed differently, so correct sorting directly saves energy and raw material.")],
              [M("Why is the handle of a cooking pan made of plastic?",
                 "Plastic is a poor conductor of heat|Plastic is shiny|Plastic is heavy|Plastic dissolves in water", 0,
                 "Insulating handles stay cool enough to hold."),
               M("Objects are grouped mainly to:",
                 "Study and use them conveniently|Make them heavier|Change their colour|Increase their price", 0,
                 "Grouping reveals shared properties so materials can be used scientifically."),
               S("Give one example each of a soluble and an insoluble substance.", "Sugar is soluble; sand is insoluble.",
                 "Sugar dissolves in water, sand does not and settles at the bottom.")]),
        ]),
        C(5, "Separation of Substances", [
            T("Handpicking, Threshing, Winnowing and Sieving",
              "Mixtures can be separated using differences in size, weight and appearance. Choosing the method "
              "depends on the difference between the components.",
              ["Handpicking removes small amounts of visible impurities such as stones from pulses.",
               "Threshing separates grain from stalks by beating or by machines.",
               "Winnowing separates lighter husk from heavier grain with wind or blowing air.",
               "Sieving separates components of different particle size, such as bran from flour."],
              [E("Farmer's sequence",
                 "After harvesting, wheat is threshed to free the grain, winnowed to blow away husk, then sieved "
                 "to remove dirt and broken grain. Each step uses a different property — size, weight, size again."),
               E("Separating a mixture of salt and sand",
                 "Neither handpicking nor winnowing works well. Add water: salt dissolves, sand does not. Filter "
                 "to remove sand, then evaporate the filtrate to recover salt.")],
              [M("Winnowing separates components based on:", "Difference in weight|Difference in colour|Solubility|Magnetism", 0,
                 "Wind carries the lighter husk away while heavier grain falls close by."),
               M("Which method removes small stones from rice?", "Handpicking|Evaporation|Condensation|Filtration", 0,
                 "Stones are visible and few, so they are removed by hand."),
               S("Why is threshing done before winnowing?", "Threshing frees grain from stalks; winnowing then removes the light husk.",
                 "You cannot blow away husk while it is still attached to the stalk.")]),
            T("Filtration, Evaporation and Solutions",
              "Solids can be separated from liquids by filtration, sedimentation and decantation; dissolved "
              "solids are recovered by evaporation and condensation.",
              ["Sedimentation lets heavy insoluble particles settle; decantation pours off the clear liquid.",
               "Filtration traps insoluble solids on filter paper, allowing the clear filtrate through.",
               "Evaporation boils off the solvent and leaves the dissolved solid behind.",
               "A solution has a solute dissolved in a solvent; a saturated solution cannot dissolve more solute at that temperature, "
               "and heating usually increases how much can dissolve."],
              [E("Clean water from muddy water",
                 "Muddy water is left to stand so mud settles (sedimentation), the clear water is poured off "
                 "(decantation) and then filtered through filter paper. It looks clear but still needs boiling "
                 "to be safe to drink, because dissolved germs are not removed by filtering."),
               E("Recovering salt from seawater",
                 "Seawater is evaporated in shallow ponds by sunlight. Water turns to vapour, salt crystals stay "
                 "behind. This is exactly how salt is produced at the coast.")],
              [M("The clear liquid that passes through filter paper is called:", "Filtrate|Residue|Solute|Solvent", 0,
                 "The liquid that passes through is the filtrate; the solid left on the paper is the residue."),
               M("Which method recovers dissolved salt from salt water?", "Evaporation|Filtration|Sieving|Winnowing", 0,
                 "Water evaporates and salt is left behind."),
               S("What is a saturated solution?", "A solution that cannot dissolve any more solute at a given temperature.",
                 "Extra solute added to a saturated solution simply settles at the bottom.")]),
        ]),
        C(6, "Changes Around Us", [
            T("Reversible and Irreversible Changes",
              "Some changes can be reversed by reversing the conditions, and some cannot. Reversibility is "
              "one of the simplest ways to describe a change.",
              ["Melting ice, folding paper, stretching a rubber band and dissolving salt are reversible.",
               "Burning paper, cooking rice, rusting iron, curdling milk and baking clay pots are irreversible.",
               "A change may be fast (burning) or slow (rusting, growth of a tree).",
               "Irreversible changes usually create a new substance with new properties."],
              [E("Reversing a change",
                 "Water freezes to ice in a freezer; ice melts back to water at room temperature. Heating and "
                 "cooling reverse each other because no new substance is formed."),
               E("An irreversible kitchen change",
                 "A raw egg cannot be turned back from a fried egg. The proteins have unfolded and bonded "
                 "differently, so no amount of cooling restores the raw egg.")],
              [M("Which of these changes is irreversible?", "Burning of paper|Melting of wax|Folding of paper|Dissolving sugar in water", 0,
                 "Burning forms ash, smoke and gases — new substances that cannot be turned back into paper."),
               M("Melting of ice is a ______ change.", "Reversible|Irreversible|Chemical|Permanent", 0,
                 "Ice can be refrozen, so the change is reversible."),
               S("Give two examples each of reversible and irreversible changes.",
                 "Reversible: melting of wax, dissolving salt. Irreversible: rusting of iron, cooking food.")]),
            T("How Changes Happen: Heating, Cooling and Expansion",
              "Changes are triggered by conditions: heating, cooling, mixing, adding water or light. Heating "
              "and cooling often cause expansion and contraction.",
              ["Most solids and liquids expand on heating and contract on cooling.",
               "A tight metal lid on a glass jar loosens when the lid is warmed, because the metal expands more than glass.",
               "Gaps are left between railway tracks and in bridges to allow expansion in summer.",
               "Dissolving is a change in which a substance spreads evenly through a liquid; the solute can be recovered."],
              [E("Loosening a stuck lid",
                 "Hold the metal lid under hot water for a few seconds. The metal expands slightly faster than "
                 "the glass, the grip loosens and the lid opens."),
               E("Why telephone wires sag",
                 "Wires are strung in winter when they are shorter. In summer they expand and sag. Engineers fix "
                 "them with the right tension so sagging does not damage them.")],
              [M("Most substances ______ on heating.", "Expand|Contract|Freeze|Evaporate", 0, "Heating increases particle spacing, so solids and liquids expand."),
               M("Gaps in railway tracks are left to allow for:", "Expansion in summer|Rainwater drainage|Faster trains|Sound travel", 0,
                 "Without gaps, expanding steel could buckle the track."),
               S("Why does a metal lid open easily after being warmed?", "The metal expands more than the glass and loosens.",
                 "Differential expansion is used to open tightly stuck lids.")]),
        ]),
        C(7, "Getting to Know Plants", [
            T("Roots, Stems and Leaves",
              "Flowering plants have roots that anchor and absorb, stems that support and transport, and "
              "leaves that make food.",
              ["Tap roots have one main root with branches (mustard, carrot); fibrous roots are a bunch of thin roots (grass, wheat).",
               "Roots absorb water and minerals; some store food (carrot, radish) or help climbing (money plant).",
               "The stem bears leaves, flowers and fruits and carries water upward through xylem and food through phloem.",
               "Leaves have a blade, petiole, midrib and veins; stomata on the surface allow gas exchange.",
               "Venation is reticulate (net-like, dicots) or parallel (monocots, grasses)."],
              [E("Reading a leaf",
                 "A mango leaf has a network of veins (reticulate) and a tap root system; a grass leaf has parallel "
                 "veins and fibrous roots. Leaf venation and root type usually match."),
               E("Why roots are pulled from the soil with difficulty",
                 "Branched roots hold the plant firmly and increase surface area for absorbing water. This is also "
                 "why plants bind soil and reduce erosion.")],
              [M("Carrot is an example of a:", "Modified tap root|Fibrous root|Stem|Leaf", 0, "Carrot stores food in its tap root."),
               M("Water is transported through the plant by:", "Xylem|Phloem|Stomata|Lamina", 0,
                 "Xylem carries water and minerals upward from the root."),
               S("State two functions of leaves.", "They make food by photosynthesis and exchange gases through stomata.",
                 "Leaves also lose water by transpiration, which helps pull water up the plant.")]),
            T("Flowers, Fruits and the Basics of Photosynthesis",
              "Flowers are reproductive structures. After pollination and fertilisation they become fruits, and "
              "seeds develop inside. Leaves make food using sunlight, water and carbon dioxide.",
              ["A flower has sepals (protect the bud), petals (attract pollinators), stamens (male, produce pollen) and pistil (female, contains ovary and ovules).",
               "Pollination is the transfer of pollen to the stigma; fertilisation is the fusion of gametes.",
               "The ovary develops into the fruit and ovules into seeds.",
               "Photosynthesis needs chlorophyll, sunlight, carbon dioxide and water, and produces glucose and oxygen.",
               "Plants release oxygen during the day and respire throughout the day and night."],
              [E("From flower to fruit",
                 "After a bee visits a pumpkin flower, pollen grains land on the stigma and grow tubes to the "
                 "ovules. The ovary swells into a pumpkin containing seeds — each seed from one fertilised ovule."),
               E("Why a plant in a dark room goes pale",
                 "Without light, chlorophyll is not made and photosynthesis stops, so leaves look yellow and the "
                 "plant slowly starves. Light is the energy source for food production.")],
              [M("The female part of a flower is the:", "Pistil|Stamen|Petal|Sepal", 0,
                 "The pistil contains the stigma, style and ovary."),
               M("Which gas is released during photosynthesis?", "Oxygen|Carbon dioxide|Nitrogen|Hydrogen", 0,
                 "Oxygen is a by-product of splitting water during photosynthesis."),
               S("Which part of the flower becomes the fruit?", "The ovary becomes the fruit; ovules become seeds.")]),
        ]),
        C(8, "Body Movements", [
            T("Bones, Joints and the Skeleton",
              "The human skeleton is a framework of bones that supports the body, protects organs and, together "
              "with muscles, allows movement. Bones meet at joints.",
              ["The skull protects the brain, the rib cage protects the heart and lungs, and the backbone protects the spinal cord.",
               "Immovable joints (skull), ball-and-socket joints (shoulder, hip), hinge joints (elbow, knee), pivot joints (neck) and gliding joints (wrist) allow different movements.",
               "A joint is where two or more bones meet; cartilage and a fluid cushion reduce friction.",
               "Bones are living tissue: they grow, repair and store calcium."],
              [E("Why the knee bends one way",
                 "The knee is a hinge joint, like a door hinge, so it allows bending and straightening in one "
                 "plane. The shoulder is a ball-and-socket joint, so the arm can swing in all directions."),
               E("The rib cage as a shield",
                 "The ribs curve around the chest and attach to the backbone and breastbone. This cage protects "
                 "the lungs and heart while still allowing the chest to expand when you breathe.")],
              [M("The elbow is an example of a:", "Hinge joint|Ball-and-socket joint|Pivot joint|Immovable joint", 0,
                 "Elbows and knees work like door hinges."),
               M("Which structure protects the brain?", "Skull|Rib cage|Backbone|Pelvis", 0, "The skull encloses the brain."),
               S("Why are joints needed?", "They allow the body to bend and move in different ways and hold bones together.",
                 "Different joint types permit different ranges of movement, from fixed skull plates to freely moving hips.")]),
            T("Muscles and Movement in Animals",
              "Muscles pull on bones to make them move; they work in pairs. Animals without bones use other "
              "systems: shells, body-fluid pressure, segmented bodies or fins.",
              ["Contracting a muscle shortens it and pulls the bone; the opposing muscle relaxes.",
               "Earthworms move with body-fluid pressure and bristles (setae) that grip the soil.",
               "Snails glide on a muscular foot and mucus; cockroaches use legs and wings attached to a segmented body.",
               "Fish swim with fins and a flexible backbone; birds have hollow bones and wings for flight."],
              [E("Bending the arm",
                 "The bicep on top of the upper arm contracts and shortens, pulling the forearm up. To straighten "
                 "the arm, the triceps contracts and the bicep relaxes. Muscles can only pull, so they work in pairs."),
               E("How an earthworm burrows",
                 "The worm lengthens by filling its front segments with fluid, anchors with bristles and then "
                 "pulls its rear forward. No bones, but the same principle: force against the surroundings.")],
              [M("Muscles can only:", "Pull|Push|Neither pull nor push|Both equally", 0,
                 "A contracting muscle shortens and pulls; pairs of muscles produce opposite movements."),
               M("Earthworms move with the help of:", "Body fluid and bristles|Bones and joints|Shells and feet|Wings", 0,
                 "Fluid pressure plus setae let the worm grip and extend its body."),
               S("Why do birds have hollow bones?", "Hollow bones make the skeleton light, helping flight.",
                 "Lightness reduces the energy needed to lift the body against gravity.")]),
        ]),
        C(9, "The Living Organisms and Their Surroundings", [
            T("Habitat and Adaptation",
              "A habitat is the place where an organism lives and gets its needs met. Organisms are adapted "
              "in structure and behaviour to survive there.",
              ["Biotic components are living (plants, animals, microbes); abiotic components are non-living (air, water, soil, light, temperature).",
               "Adaptations can be structural (camel's hump), behavioural (migration) or physiological (sweating).",
               "Terrestrial habitats include deserts, grasslands and forests; aquatic habitats include ponds, rivers and oceans.",
               "Cacti have spines instead of leaves, thick waxy stems and deep roots to conserve water.",
               "Fish have gills to breathe dissolved oxygen and streamlined bodies to move through water."],
              [E("The camel's survival kit",
                 "A camel stores fat in its hump, has long eyelashes to keep out sand, nostrils it can close, "
                 "and wide padded feet. It can lose water slowly and tolerate high body temperature — every feature "
                 "is an answer to desert conditions."),
               E("From water to land: the frog",
                 "A tadpole has gills and a tail and lives in water. As it becomes a frog it develops lungs and "
                 "legs. The same animal occupies two habitats with two sets of adaptations at different life stages.")],
              [M("The camel's hump stores:", "Fat|Water|Sand|Air", 0,
                 "The hump is a fat store that can be broken down for energy; it is not a water bag."),
               M("Gills help fish to:", "Breathe oxygen dissolved in water|Swim faster|Float on water|Smell food", 0,
                 "Gills absorb dissolved oxygen from water."),
               S("Define habitat.", "The place where an organism lives and obtains food, water, shelter and air.")]),
            T("Acclimatisation and Life in Extreme Places",
              "Acclimatisation is a short-term adjustment to a new environment. Organisms also survive extreme "
              "places with remarkable specialisations.",
              ["Acclimatisation happens within a lifetime and is reversible, unlike evolutionary adaptation.",
               "People moving to high mountains make more red blood cells after some weeks, so they can carry more oxygen.",
               "Some deep-sea fish produce light (bioluminescence); desert plants open stomata at night to save water.",
               "About 70% of Earth is covered by water, and most organisms live in water."],
              [E("Training at altitude",
                 "Athletes train in the hills before a competition. Lower oxygen forces the body to make more red "
                 "blood cells, so they perform better when they return to sea level."),
               E("Why sea mammals surface",
                 "Dolphins and whales breathe with lungs, so they must come up for air. Their nostrils sit on top "
                 "of the head, an adaptation that lets them breathe without slowing down.")],
              [M("Acclimatisation is:", "A short-term adjustment to the environment|A permanent genetic change|A type of habitat|A food chain", 0,
                 "It is a reversible, within-lifetime adjustment."),
               M("The percentage of Earth's surface covered by water is about:", "70%|30%|50%|90%", 0,
                 "Water covers roughly 71% of the planet, and it makes up most of the living space."),
               S("Why do people living in mountains have more red blood cells?",
                 "Thin air has less oxygen, so more red blood cells are needed to carry enough oxygen.")]),
        ]),
        C(10, "Motion and Measurement of Distances", [
            T("Measurement, Units and Correct Method",
              "Measurement means comparing a quantity with a standard unit. Standard units are needed so that "
              "measurements mean the same thing everywhere.",
              ["The SI unit of length is the metre (m); 1 m = 100 cm, 1 km = 1000 m.",
               "A horizontal distance is measured with a metre scale, a curved line with a string, and long distances with a surveyor's tape or a trundle wheel.",
               "The eye must be directly above the scale marks to avoid parallax error.",
               "The scale should touch the object and zero should coincide with one end; if the zero is broken, start from another mark and subtract.",
               "Decimal units make multiplication and conversion simple: 1.5 m = 150 cm."],
              [E("Measuring a curve correctly",
                 "To measure the length of a curved leaf edge, place a thread along the edge, mark the ends on "
                 "the thread, then straighten it against a scale. Straight rulers cannot follow curves accurately."),
               E("Broken zero",
                 "If a ruler is broken at the zero mark, place the object starting at the 2.0 cm mark. If the "
                 "other end reads 12.5 cm, the length is 12.5 − 2.0 = 10.5 cm.")],
              [M("The SI unit of length is the:", "Metre|Centimetre|Kilometre|Foot", 0, "The metre is the SI base unit of length."),
               M("1.5 m equals:", "150 cm|15 cm|1500 cm|0.15 cm", 0, "1 m = 100 cm, so 1.5 m = 150 cm."),
               S("How would you measure the length of a curved line?",
                 "Place a thread along the curve, mark the ends, straighten the thread and measure it with a scale.")]),
            T("Types of Motion",
              "Motion is a change of position with time. It can be straight-line, circular, periodic, "
              "oscillatory or rotational, and the same object can show more than one type.",
              ["Rectilinear motion: a car on a straight road.",
               "Circular motion: a point on a wheel, the motion of the Moon around Earth.",
               "Periodic motion repeats at equal time intervals; oscillatory motion moves to and fro about a mean position.",
               "Rotational motion: the spinning of a top about a fixed axis.",
               "Objects like a sewing machine needle show oscillatory motion while the wheel shows circular motion."],
              [E("A child on a swing",
                 "The swing moves to and fro about its lowest point, so it is oscillatory and also periodic. The "
                 "path is part of a circle, so it also has a circular aspect."),
               E("The Moon",
                 "The Moon travels around Earth (circular, periodic motion) while also rotating about its own axis. "
                 "One object, two motions at once.")],
              [M("The motion of a point on a fan blade is:", "Circular|Rectilinear|Oscillatory|Random", 0,
                 "A point on a rotating blade traces a circle."),
               M("A motion that repeats at equal intervals is called:", "Periodic|Circular|Random|Uniform", 0,
                 "Periodic motion returns to the same state again and again."),
               S("Give one example each of rectilinear and oscillatory motion.",
                 "A car on a straight road (rectilinear) and a swinging pendulum (oscillatory).")]),
        ]),
        C(11, "Light, Shadows and Reflections", [
            T("Light, Objects and Shadows",
              "Light travels in straight lines. When an opaque object blocks light, a shadow forms behind it. "
              "Materials are transparent, translucent or opaque.",
              ["Light enables us to see things; we see an object when light from it reaches our eyes.",
               "Transparent: clear glass; translucent: frosted glass or butter paper; opaque: wood, cardboard.",
               "A shadow forms on a screen when an opaque object blocks light; it has the same shape as the object.",
               "In a pinhole camera, light travels in straight lines and forms an upside-down image.",
               "Shadows are larger when the object is closer to the light source."],
              [E("Shadow size investigation",
                 "Hold a ball between a torch and a wall. Move the ball towards the torch and the shadow on the "
                 "wall becomes bigger; move it towards the wall and the shadow shrinks. Size depends on the "
                 "geometry of light travelling in straight lines."),
               E("The pinhole camera",
                 "Place a small hole in one side of a box and tracing paper on the other. A candle outside forms "
                 "an inverted image on the paper — proof that light travels in straight lines and crosses at the hole.")],
              [M("A shadow is formed by:", "An opaque object blocking light|A transparent object|A mirror reflecting light|A light source alone", 0,
                 "Only a light-blocking object produces a shadow."),
               M("In a pinhole camera the image is:", "Upside down|Upright|Always blue|Not formed", 0,
                 "Rays cross at the hole, so the image is inverted."),
               S("Classify materials as transparent, translucent or opaque: clear glass, butter paper, wood.",
                 "Clear glass is transparent, butter paper is translucent and wood is opaque.")]),
            T("Mirrors and Reflection",
              "Plane mirrors reflect light and form images that are virtual, erect and laterally inverted. "
              "Curved mirrors are used as magnifiers and as rear-view mirrors.",
              ["Reflection occurs when light bounces off a surface; a plane mirror gives a virtual image of the same size.",
               "In a plane mirror, the image is as far behind the mirror as the object is in front.",
               "Lateral inversion swaps left and right, which is why an ambulance has mirror-image writing.",
               "A convex mirror shows a wider view and makes images smaller; a concave mirror can magnify.",
               "A periscope uses two plane mirrors at 45° to see over obstacles."],
              [E("Why writing looks reversed in a mirror",
                 "Raise your right hand in front of a mirror: the image raises its left hand. The mirror does not "
                 "swap up and down, it swaps left and right — lateral inversion."),
               E("The periscope",
                 "Light from the object strikes the top mirror, is reflected down to a second mirror and reaches "
                 "the eye. Submarines and periscopes use this to see above water while staying hidden.")],
              [M("The image formed by a plane mirror is:", "Virtual and erect|Real and inverted|Real and erect|Always magnified", 0,
                 "The image cannot be caught on a screen and is upright."),
               M("A convex mirror is used as a rear-view mirror because it:",
                 "Gives a wider field of view|Magnifies the traffic|Inverts the image|Blocks sunlight", 0,
                 "A wider view shows more of the road behind."),
               S("Why does an ambulance carry 'AMBULANCE' written in reverse?",
                 "So that drivers reading it in a mirror see it correctly, because a plane mirror laterally inverts the image.")]),
        ]),
        C(12, "Electricity and Circuits", [
            T("The Electric Cell and a Simple Circuit",
              "An electric cell drives current around a closed circuit. Bulbs glow only when the circuit is "
              "complete; a switch opens or closes the path.",
              ["A cell has a positive terminal (+) and a negative terminal (−); current flows from + to − outside the cell.",
               "A bulb has a filament that glows when current passes; the bulb's metal casing and tip connect the filament.",
               "The circuit must be closed for current to flow; a break stops the current immediately.",
               "Conductors allow current (metals, graphite); insulators block it (rubber, plastic, dry wood).",
               "Do not connect the two terminals of a cell with a wire directly — the cell can overheat."],
              [E("Why the bulb does not glow",
                 "Check three things: the cell is not dead, the bulb is not fused and every connection is tight. "
                 "A loose wire breaks the circuit, so no current flows."),
               E("Making a torch",
                 "A cell, a bulb, a switch and wires form a simple torch circuit. Pressing the switch closes the "
                 "circuit, current flows through the filament and light is produced.")],
              [M("Electric current flows in a circuit only when it is:", "Closed|Open|Broken|Disconnected", 0,
                 "A complete, closed path is needed."),
               M("Which of these is a conductor?", "Copper wire|Rubber band|Plastic comb|Glass rod", 0,
                 "Metals such as copper carry current."),
               S("How can you test whether a material is a conductor or insulator?",
                 "Connect it in a simple circuit with a cell and bulb; if the bulb glows it is a conductor.")]),
            T("Circuit Components, Symbols and Safety",
              "Electric circuits are drawn with standard symbols. Safety rules prevent shocks and fires.",
              ["Symbols: a straight line for a wire, a long and short parallel line for a cell, a circle with a cross for a bulb.",
               "A switch is shown as a break in the wire with a lever arm.",
               "Never touch electric switches with wet hands; water conducts electricity.",
               "Do not use damaged wires or overload sockets; a short circuit can cause fire.",
               "Electric current in household wires comes from the mains and is much stronger and more dangerous than a cell."],
              [E("Reading a circuit diagram",
                 "A rectangle of straight lines with a cell symbol, a bulb symbol and a switch symbol describes a "
                 "complete circuit. If the switch symbol is open, the bulb is off."),
               E("Why wet hands are dangerous",
                 "Water with dissolved salts conducts electricity, so wet skin lowers resistance. Current can pass "
                 "through the body, which is why switches are never touched with wet hands.")],
              [M("The symbol of a cell in a circuit diagram is:", "A long and a short parallel line|A circle with a cross|A zigzag line|A rectangle", 0,
                 "The long line is the positive terminal and the short line the negative terminal."),
               M("Water conducts electricity because it contains:", "Dissolved salts|Air|Plastic|Rubber", 0,
                 "Dissolved salts provide ions that carry charge."),
               S("Write two electric safety rules for home.", "Never touch switches with wet hands; never overload a socket or use damaged wires.")]),
        ]),
        C(13, "Fun with Magnets", [
            T("Magnetic Materials and Poles",
              "Magnets attract iron, nickel and cobalt, and have two poles where the effect is strongest. A "
              "free-suspended magnet always points north–south.",
              ["A magnet's ends are its north and south poles; like poles repel, unlike poles attract.",
               "A freely suspended bar magnet aligns along the Earth's north–south direction; the end pointing north is the north pole.",
               "Magnets attract magnetic materials, not all metals (copper and aluminium are not attracted).",
               "A compass is a small magnet that indicates direction, used by sailors and travellers.",
               "Magnetic force acts through air and even through some materials, and is strongest near the poles."],
              [E("Finding north without a compass",
                 "Tie a bar magnet with a thread and let it hang freely. After it settles, the pole pointing towards "
                 "geographic north is the magnet's north pole. Earth itself behaves like a giant magnet."),
               E("The attraction test",
                 "A magnet picks up iron nails and steel pins but not copper coins or aluminium foil. Attraction "
                 "is a test for magnetic material, not for 'being a metal'.")],
              [M("Which pair of poles attracts?", "North and south|North and north|South and south|All pairs repel", 0,
                 "Unlike poles attract, like poles repel."),
               M("Which of these is NOT attracted by a magnet?", "Copper coin|Iron nail|Nickel pin|Cobalt clip", 0,
                 "Copper is not a magnetic material."),
               S("How does a compass help in finding direction?",
                 "Its magnetised needle aligns along Earth's magnetic field and points north–south.")]),
            T("Making Magnets and Demagnetisation",
              "Magnets can be made by stroking or by an electric current, and can lose magnetism when heated, "
              "dropped or stored carelessly.",
              ["Stroke a piece of iron in one direction with one pole of a magnet, repeatedly, to magnetise it.",
               "An electromagnet is a coil of wire around an iron core; it is magnetic only while current flows.",
               "Heating, hammering or dropping a magnet can demagnetise it.",
               "Store magnets in pairs with opposite poles together and a piece of iron across them, to preserve strength.",
               "Magnets should be kept away from mobile phones and music players."],
              [E("A simple electromagnet",
                 "Wind 30 turns of insulated copper wire around an iron nail and connect the ends to a cell. The "
                 "nail picks up pins while the circuit is on and drops them when it is switched off."),
               E("Why compasses are stored carefully",
                 "A compass needle is a weak magnet. Keeping it beside strong magnets or dropping it can reverse "
                 "or weaken the needle, making direction readings unreliable.")],
              [M("An electromagnet loses its magnetism when:", "Current is switched off|It is cooled|It is painted|It is weighed", 0,
                 "Magnetism depends on the flowing current."),
               M("To demagnetise a magnet you can:", "Heat it strongly|Paint it|Wrap it in paper|Wash it", 0,
                 "High temperature, hammering or dropping disturb the alignment of domains."),
               S("How should two bar magnets be stored?", "In pairs with opposite poles together and a soft iron piece across the ends.")]),
        ]),
        C(14, "Water", [
            T("The Water Cycle",
              "Water moves continuously between the oceans, atmosphere and land in the water cycle, driven by "
              "the Sun's heat.",
              ["Evaporation changes water into vapour; condensation changes vapour back into droplets; precipitation is rain, hail or snow.",
               "Transpiration releases water vapour from plant leaves and adds to atmospheric moisture.",
               "Groundwater seeps into the soil and collects above an impermeable layer; wells and boreholes reach it.",
               "The demand for water depends on rainfall patterns and how much is used for farming, industry and homes.",
               "Water is a universal solvent, which is why most substances dissolve in it."],
              [E("The water cycle in a rainy week",
                 "Sun heats a lake, water evaporates, rises, cools and condenses into clouds, and finally falls as "
                 "rain. The rain flows back to the lake through streams. The same water keeps circulating."),
               E("Why plants matter in the cycle",
                 "A single mature tree can release hundreds of litres of water vapour a day through transpiration. "
                 "Cutting forests reduces this flow and can make an area drier.")],
              [M("The process of changing water vapour into liquid is:", "Condensation|Evaporation|Filtration|Precipitation", 0,
                 "Cooling vapour forms droplets."),
               M("Water that collects underground is called:", "Groundwater|Rainwater|Surface water|Sea water", 0,
                 "Water that seeps into the soil and fills the spaces above impermeable rock is groundwater."),
               S("List the steps of the water cycle.", "Evaporation, condensation, precipitation and collection (runoff and groundwater).")]),
            T("Water Conservation and Rainwater Harvesting",
              "Fresh water is limited, so it must be used carefully. Rainwater harvesting, drip irrigation and "
              "leak repair all save water.",
              ["Rainwater harvesting collects roof rainwater and stores it or sends it into the ground to recharge groundwater.",
               "Drip irrigation delivers water directly to plant roots and wastes much less than flood irrigation.",
               "Fixing leaking taps, closing taps while brushing and reusing washing water for plants save litres every day.",
               "Dams and lakes store water and recharge groundwater but can displace people and affect rivers.",
               "A drought is a long period of unusually low rainfall; a flood is an overflow of water onto normally dry land."],
              [E("Harvesting a rooftop",
                 "A 100 m^2^ roof with 50 mm of rain can collect about 5,000 litres (100 × 0.05 m × 1000). "
                 "Piped into a tank or a recharge pit, that water is saved instead of running down the drain."),
               E("Drip versus flood irrigation",
                 "Flood irrigation can lose more than half the water to evaporation and runoff. Drip irrigation "
                 "delivers water drop by drop at the root and can save 30–60% of water.")],
              [M("Drip irrigation is useful because it:",
                 "Delivers water directly to roots and saves water|Floods the field|Uses sea water|Needs no plants", 0,
                 "It minimises evaporation and runoff."),
               M("Rainwater harvesting mainly helps to:",
                 "Recharge groundwater and store water|Increase rainfall|Filter sea water|Produce electricity", 0,
                 "Captured rain is stored or allowed to percolate into the ground."),
               S("Give three ways to save water at home.",
                 "Fix leaks, turn off taps while brushing, reuse water for plants (also take shorter showers).")]),
        ]),
        C(15, "Air Around Us", [
            T("Composition of Air",
              "Air is a mixture of gases. Nitrogen makes up about 78%, oxygen about 21%, and the rest is argon, "
              "carbon dioxide, water vapour and dust.",
              ["Air is a mixture, so its components can be separated by physical means and keep their own properties.",
               "Oxygen supports burning; nitrogen does not; carbon dioxide puts out fire and is used in fire extinguishers.",
               "Water vapour condenses on cold surfaces, showing that air contains moisture.",
               "Dust particles make a beam of sunlight visible and settle on surfaces.",
               "Air is needed by all living things: plants and animals use oxygen for respiration."],
              [E("The candle experiment",
                 "Place a burning candle inside an inverted glass over water. As oxygen is used up, the flame "
                 "goes out and water rises into the glass, roughly one-fifth of the way — evidence that oxygen is "
                 "about a fifth of air."),
               E("Why the sky looks blue",
                 "Tiny gas molecules scatter short blue wavelengths more than long red ones. That scattered light "
                 "reaches our eyes from all directions, making the sky appear blue.")],
              [M("The gas present in the largest amount in air is:", "Nitrogen|Oxygen|Carbon dioxide|Argon", 0,
                 "Nitrogen makes up about 78% of the atmosphere."),
               M("Which gas supports burning?", "Oxygen|Nitrogen|Carbon dioxide|Water vapour", 0,
                 "Combustion needs oxygen."),
               S("Why does a burning candle go out when covered by a glass?",
                 "The oxygen inside is used up, so combustion cannot continue.")]),
            T("Life, Air and the Balance of Gases",
              "Living things depend on air. Plants add oxygen and remove carbon dioxide, keeping the balance "
              "of gases steady.",
              ["Respiration uses oxygen and releases carbon dioxide; photosynthesis does the reverse.",
               "Plants release oxygen during the day; at night only respiration occurs, but oxygen use is small compared with the ocean and forest reserves.",
               "Air pollution from burning fuels adds harmful gases and particles, causing asthma and acid rain.",
               "Green plants act as the lungs of the planet and should be protected."],
              [E("Oxygen in a sealed jar",
                 "A mouse in a sealed jar uses up oxygen and dies; adding a green plant with light restores oxygen "
                 "by photosynthesis and the mouse survives longer. This classic experiment shows the gas exchange between plants and animals."),
               E("Why cities need trees",
                 "A tree filters dust, absorbs carbon dioxide and releases oxygen. A street lined with trees can "
                 "be several degrees cooler and noticeably cleaner than a bare one.")],
              [M("During photosynthesis plants take in:", "Carbon dioxide|Oxygen|Nitrogen|Argon", 0,
                 "Carbon dioxide is the carbon source for making food."),
               M("Air pollution can cause:", "Respiratory problems|Better eyesight|Stronger bones|More oxygen", 0,
                 "Particles and gases irritate the lungs and worsen asthma."),
               S("How do plants help maintain the balance of gases in air?",
                 "They take in carbon dioxide and release oxygen during photosynthesis, balancing respiration.")]),
        ]),
        C(16, "Garbage In, Garbage Out", [
            T("Waste and Disposal",
              "Waste comes from homes, markets, farms and factories. It can be biodegradable (rottable) or "
              "non-biodegradable (not rotted by microbes).",
              ["Biodegradable waste: vegetable peels, paper, leftover food, leaves.",
               "Non-biodegradable waste: plastics, glass, metals, polythene bags.",
               "Landfills bury waste; when badly managed they attract flies, rats and stray animals and leak harmful liquids.",
               "Composting converts biodegradable waste into manure with the help of microbes; vermicomposting uses earthworms.",
               "Burning waste releases toxic gases and should be avoided."],
              [E("Making compost at home",
                 "Collect fruit and vegetable peels in a covered bin, add dry leaves in layers, keep it moist and "
                 "turn it every few days. In about two months, dark crumbly compost is ready for plants."),
               E("Why an open dump is unhealthy",
                 "Open dumps breed flies and mosquitoes, smell bad and allow rainwater to carry harmful liquids "
                 "into the soil and groundwater.")],
              [M("Which waste is biodegradable?", "Vegetable peels|Plastic bag|Glass bottle|Aluminium can", 0,
                 "Peels are broken down by microorganisms."),
               M("Vermicomposting uses:", "Earthworms|Fungi only|Bacteria only|Plastic", 0,
                 "Earthworms consume organic waste and produce nutrient-rich castings."),
               S("What is the difference between biodegradable and non-biodegradable waste? Give one example of each.",
                 "Biodegradable waste is broken down by living organisms (peels); non-biodegradable waste is not (plastic).")]),
            T("Reduce, Reuse and Recycle",
              "The best waste is the waste we never create. The 3Rs — reduce, reuse, recycle — cut pollution "
              "and save resources.",
              ["Reduce: carry a cloth bag, avoid unnecessary packaging, print less.",
               "Reuse: refill bottles, use both sides of paper, donate old clothes and books.",
               "Recycle: paper, glass, metal and some plastics can be processed into new products.",
               "Recycling paper saves trees and water and reduces landfill volume.",
               "Plastic takes hundreds of years to decompose and harms animals that swallow it."],
              [E("Recycling paper",
                 "Old newspapers are shredded, soaked, pulped and pressed into new sheets. Recycling one tonne "
                 "of paper saves roughly 17 trees and thousands of litres of water."),
               E("The cloth bag habit",
                 "A single cloth bag reused daily for a year replaces hundreds of thin plastic bags. That is "
                 "reducing waste at the source instead of cleaning it up later.")],
              [M("The 3Rs of waste management are:",
                 "Reduce, Reuse, Recycle|Read, Run, Rest|Remove, Return, Rebuild|Reduce, Replace, Repair", 0,
                 "These three strategies cut waste and conserve resources."),
               M("Recycling paper helps mainly by:",
                 "Saving trees and water|Increasing pollution|Making plastic|Keeping animals", 0,
                 "Recycling reduces the need to cut trees and saves energy and water."),
               S("Give two ways you can reduce plastic use at home.",
                 "Carry a cloth bag for shopping; refill bottles instead of buying new ones.")]),
        ]),
    ],
)
