import json

compatibility_data = {
    "Aries": {
    "Aries": {
        "overall": 80,
        "communication": 70,
        "emotional": 60,
        "intimacy": 85,
        "overall_explanation": "You're both fiery, passionate, and love to lead—but that means neither of you likes giving in. The spark is real, but so is the friction.",
        "communication_explanation": "You speak the same bold language, but neither of you likes backing down. Arguments can spark fast—but so can laughter.",
        "emotional_explanation": "You tend to keep emotions on the move, not sitting with them for long. That's fine until you both hit a vulnerable patch and no one knows how to hold space.",
        "intimacy_explanation": "This is where the fire lives. You match each other's passion beat for beat—bold, physical, and unapologetically intense."
    },
    "Taurus": {
        "overall": 65,
        "communication": 50,
        "emotional": 70,
        "intimacy": 80,
        "overall_explanation": "Taurus brings calm and you bring fire. There's a chance to complement each other—but it's not always an easy balance.",
        "communication_explanation": "You may feel like you're always the one pushing while Taurus is... just still. Their calm can soothe you—or drive you up the wall.",
        "emotional_explanation": "Taurus offers you a kind of grounding you didn't know you needed, but you might find their emotional pace frustratingly slow.",
        "intimacy_explanation": "The physical chemistry is strong, even if the rhythm takes time to align. When it does, it's steady and satisfying."
    },
    "Gemini": {
        "overall": 75,
        "communication": 85,
        "emotional": 60,
        "intimacy": 70,
        "overall_explanation": "You both love excitement, movement, and variety. Things stay fun—but may skim the surface emotionally.",
        "communication_explanation": "You'll love how quick and clever Gemini is. Conversation feels like a game you never want to stop playing.",
        "emotional_explanation": "You both tend to skip emotional depth in favor of keeping things light, which works—until one of you wants more.",
        "intimacy_explanation": "It's fun, flirty, and curious. You keep each other guessing, but that may come at the cost of deeper connection."
    },
    "Cancer": {
        "overall": 60,
        "communication": 50,
        "emotional": 75,
        "intimacy": 65,
        "overall_explanation": "You move fast and speak loud, while Cancer feels deeply and carefully. You could help each other grow—or end up hurting each other unintentionally.",
        "communication_explanation": "You say what you mean. Cancer *feels* what you mean—and that difference can get messy fast.",
        "emotional_explanation": "Cancer brings you closer to your softer side, if you're willing to meet them halfway. But if you bulldoze their feelings, they'll shut down.",
        "intimacy_explanation": "There's warmth here, and if you're gentle with them, that intimacy can grow into something surprisingly tender."
    },
    "Leo": {
        "overall": 85,
        "communication": 75,
        "emotional": 70,
        "intimacy": 90,
        "overall_explanation": "This is a fiery, magnetic match full of energy, pride, and passion. Just be mindful—two stars can't shine if they keep fighting for the spotlight.",
        "communication_explanation": "You both love to speak your mind—and take up space. Just be careful you're not talking over each other.",
        "emotional_explanation": "There's pride on both sides, which can get in the way of vulnerability. But when you both open up, it's full-on devotion.",
        "intimacy_explanation": "Fire meets fire here. The chemistry is magnetic, dramatic, and deeply satisfying when egos stay in check."
    },
    "Virgo": {
        "overall": 55,
        "communication": 60,
        "emotional": 50,
        "intimacy": 60,
        "overall_explanation": "You charge in, Virgo analyzes. The pace is off, but if you both respect the other's rhythm, there's room to meet in the middle.",
        "communication_explanation": "Virgo picks things apart; you just want to go. You may feel criticized when they're just trying to help.",
        "emotional_explanation": "You want fire, they want stability. It's easy to miss each other emotionally unless you're both making the effort.",
        "intimacy_explanation": "The spark can be there, but it won't ignite unless there's real trust. Patience matters more than passion here."
    },
    "Libra": {
        "overall": 70,
        "communication": 80,
        "emotional": 65,
        "intimacy": 75,
        "overall_explanation": "Libra smooths your rough edges, and you bring fire to their calm. The balance can be beautiful—if you don't rush or overwhelm them.",
        "communication_explanation": "Libra smooths your rough edges, and you bring fire to their indecision. It's an unexpectedly strong balance—if you don't rush them.",
        "emotional_explanation": "You crave directness, they prefer harmony. Sometimes that means they won't say what they really feel.",
        "intimacy_explanation": "The attraction is magnetic, even if it comes in waves. You'll enjoy the dance—as long as you're willing to slow down."
    },
    "Scorpio": {
        "overall": 65,
        "communication": 55,
        "emotional": 70,
        "intimacy": 80,
        "overall_explanation": "There's passion and power here, but also potential for emotional intensity that burns too hot if you're not careful.",
        "communication_explanation": "You're both intense in your own way, and neither of you forgets a slight. Conversations can feel like battles unless you're careful.",
        "emotional_explanation": "Scorpio makes you feel more than you expect, which can be both thrilling and unnerving. You'll have to earn their trust.",
        "intimacy_explanation": "This can be raw, passionate, and deeply bonding—if you're not afraid to be exposed."
    },
    "Sagittarius": {
        "overall": 90,
        "communication": 80,
        "emotional": 75,
        "intimacy": 85,
        "overall_explanation": "You've met your match in energy and spontaneity. This is one of the most natural and exciting pairings for you.",
        "communication_explanation": "You get each other. No filters, no fluff—just energy, ideas, and adventure.",
        "emotional_explanation": "Neither of you likes emotional heaviness, but you still manage to connect in a way that feels real and free.",
        "intimacy_explanation": "Playful, fiery, and bold. You match in appetite and spontaneity—it rarely gets boring."
    },
    "Capricorn": {
        "overall": 50,
        "communication": 45,
        "emotional": 55,
        "intimacy": 60,
        "overall_explanation": "This pairing needs work. You're spontaneous, they're calculated. It can feel like you're living in two different speeds.",
        "communication_explanation": "Capricorn plans, you act. You may feel they're too serious, while they think you're reckless.",
        "emotional_explanation": "You express yourself fast and loud; they hold it all in. Emotional rhythm is a challenge here.",
        "intimacy_explanation": "The connection builds slowly—if at all. But when it does, it's surprisingly grounded, even if not wildly passionate."
    },
    "Aquarius": {
        "overall": 75,
        "communication": 80,
        "emotional": 65,
        "intimacy": 70,
        "overall_explanation": "The energy here is exciting and fresh. You share independence, curiosity, and a spark that feels alive—if not always emotionally deep.",
        "communication_explanation": "Ideas bounce around effortlessly. You love how Aquarius thinks, even if they can be emotionally distant.",
        "emotional_explanation": "You want sparks; they want space. It can work if you respect each other's quirks instead of trying to change them.",
        "intimacy_explanation": "It's exciting and experimental, but may lack the emotional depth you crave—especially over time."
    },
    "Pisces": {
        "overall": 60,
        "communication": 55,
        "emotional": 70,
        "intimacy": 65,
        "overall_explanation": "You're bold and upfront, Pisces is gentle and dreamy. This can be a soft and sweet bond—or a constant mismatch of energy.",
        "communication_explanation": "You're direct, they're dreamy. Sometimes you wonder if you're speaking the same language.",
        "emotional_explanation": "Pisces feels deeply and gives a lot, but may get overwhelmed by your intensity. Tread gently.",
        "intimacy_explanation": "There's sweetness here if you slow down. Pisces wants connection, not just heat—and you might surprise yourself by wanting that too."
    }
},
    "Taurus": {
    "Aries": {
        "overall": 65,
        "communication": 50,
        "emotional": 70,
        "intimacy": 80,
        "overall_explanation": "You crave peace and grounding, while Aries brings a whirlwind of fire. This can either thrill you—or exhaust you.",
        "communication_explanation": "Aries moves fast, you like to take your time. If they rush you or ignore your silence, things get tense quickly.",
        "emotional_explanation": "You offer emotional steadiness, which Aries needs more than they admit—but their intensity may wear you down.",
        "intimacy_explanation": "Once the rhythm is found, this becomes a surprisingly passionate match. Aries brings spark, you bring depth."
    },
    "Taurus": {
        "overall": 90,
        "communication": 80,
        "emotional": 85,
        "intimacy": 90,
        "overall_explanation": "This is a pairing built for the long haul—stable, loyal, and deeply sensual. You both understand each other without needing much noise.",
        "communication_explanation": "You communicate in similar ways: calm, grounded, and with intent. It feels like you're always on the same page.",
        "emotional_explanation": "There's a shared emotional safety here. You both give generously without drama or games.",
        "intimacy_explanation": "Sensuality is second nature to both of you. There's comfort and fire here—an intimacy that deepens over time."
    },
    "Gemini": {
        "overall": 60,
        "communication": 70,
        "emotional": 50,
        "intimacy": 65,
        "overall_explanation": "You want roots; Gemini wants wings. It's not impossible, but it requires more compromise than comfort.",
        "communication_explanation": "You value thoughtful, slow-moving conversations. Gemini flits between topics. It can feel like you're never quite catching up.",
        "emotional_explanation": "Gemini doesn't always pause to feel, and you need emotional presence. This can leave you feeling unseen.",
        "intimacy_explanation": "The attraction may start strong, but staying connected physically takes effort unless emotional trust builds."
    },
    "Cancer": {
        "overall": 85,
        "communication": 75,
        "emotional": 90,
        "intimacy": 80,
        "overall_explanation": "You both love home, comfort, and devotion. This bond feels warm and natural—like something that grows quietly but beautifully.",
        "communication_explanation": "There's a gentle flow here. Neither of you pushes too hard, and you genuinely care about what the other feels.",
        "emotional_explanation": "Your emotional energies align well. You both want security and affection, and you're willing to show up for each other.",
        "intimacy_explanation": "Tender, sensual, and deeply emotional. The intimacy here can feel like a sacred space if nurtured with care."
    },
    "Leo": {
        "overall": 75,
        "communication": 70,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "You're both strong in your own way—Leo wants to shine, and you want to feel safe. If mutual respect exists, this becomes a power couple.",
        "communication_explanation": "Leo loves attention; you prefer quiet loyalty. If you can admire each other's differences, conversations become more generous.",
        "emotional_explanation": "There's passion and pride on both sides. You'll need to learn when to step forward—and when to soften.",
        "intimacy_explanation": "Leo brings fire, you bring depth. Together, you create a romantic and magnetic intimacy that feels both glamorous and grounded."
    },
    "Virgo": {
        "overall": 80,
        "communication": 85,
        "emotional": 75,
        "intimacy": 80,
        "overall_explanation": "You both thrive on stability and care in the details. It's not a whirlwind romance—but it's a deeply respectful and enduring one.",
        "communication_explanation": "You speak in calm, practical ways. Virgo listens with care, and you feel heard without needing to shout.",
        "emotional_explanation": "Emotions are expressed more in action than in words—but there's comfort in that mutual understanding.",
        "intimacy_explanation": "There's something quietly passionate here. Intimacy unfolds slowly, but it's thoughtful and real when it arrives."
    },
    "Libra": {
        "overall": 85,
        "communication": 90,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "This is an elegant match—beauty, balance, and charm define your connection. Together, you create harmony people envy.",
        "communication_explanation": "Libra's grace softens your stubborn streak, while your steadiness grounds their indecision. Conversation flows effortlessly.",
        "emotional_explanation": "You both seek peace, and emotional tension is rarely explosive. Instead, there's a mutual desire to keep each other emotionally content.",
        "intimacy_explanation": "Sensual, romantic, and aesthetically pleasing—this pairing feels like a love story written in soft light."
    },
    "Scorpio": {
        "overall": 80,
        "communication": 70,
        "emotional": 85,
        "intimacy": 90,
        "overall_explanation": "This is a deeply intense bond. You both crave loyalty and depth, but you move differently—one grounded, one brooding.",
        "communication_explanation": "Scorpio speaks in riddles and emotion; you speak in facts and calm tones. Learning each other's language is key.",
        "emotional_explanation": "You both want emotional loyalty and trust—but Scorpio needs more depth than you may be used to. When you give it, it changes everything.",
        "intimacy_explanation": "The sexual chemistry here runs deep and lasting. Physical touch becomes an emotional language for you both."
    },
    "Sagittarius": {
        "overall": 60,
        "communication": 65,
        "emotional": 55,
        "intimacy": 70,
        "overall_explanation": "You want calm and consistency, while Sagittarius wants freedom and thrill. This can work—but only if both respect each other's world.",
        "communication_explanation": "They joke when you want to be serious, and you may feel they're always halfway out the door. It's tricky to sync.",
        "emotional_explanation": "Sagittarius avoids emotional heaviness. You may feel like they gloss over things you take seriously.",
        "intimacy_explanation": "The chemistry can be fun and playful, but may lack the emotional depth and patience you crave in the long run."
    },
    "Capricorn": {
        "overall": 90,
        "communication": 80,
        "emotional": 85,
        "intimacy": 90,
        "overall_explanation": "This is a powerfully grounded match—stable, committed, and quietly passionate. You build something solid together.",
        "communication_explanation": "You both speak with purpose and respect. There's no need for fluff—just mutual understanding and shared goals.",
        "emotional_explanation": "You value loyalty and show love through consistency, not drama. Capricorn respects that deeply.",
        "intimacy_explanation": "This may not be wild passion at first, but it runs deep and steady—like a fire that's built to last."
    },
    "Aquarius": {
        "overall": 50,
        "communication": 60,
        "emotional": 45,
        "intimacy": 55,
        "overall_explanation": "You want warmth and presence; Aquarius wants freedom and space. You may feel like they're always somewhere else.",
        "communication_explanation": "You prefer face-to-face connection; Aquarius sometimes feels distant, even when right in front of you.",
        "emotional_explanation": "They can be detached and abstract with feelings, while you long for real, emotional closeness.",
        "intimacy_explanation": "Things can feel experimental or aloof. Unless you both make real effort, intimacy might lack emotional richness."
    },
    "Pisces": {
        "overall": 70,
        "communication": 65,
        "emotional": 80,
        "intimacy": 75,
        "overall_explanation": "You both feel deeply and care quietly. This bond can be gentle and soulful, but it needs boundaries to stay balanced.",
        "communication_explanation": "Pisces may be too vague at times, while you prefer clarity. But their softness draws out your more tender side.",
        "emotional_explanation": "You provide the stability they crave, and they remind you to open up emotionally. It's a nurturing emotional loop when it works.",
        "intimacy_explanation": "There's sweetness and surrender here. If you trust each other, the connection becomes soft, sensual, and meaningful."
    }
},
    "Gemini": {
    "Aries": {
        "overall": 75,
        "communication": 85,
        "emotional": 60,
        "intimacy": 70,
        "overall_explanation": "You're both fast-moving and love variety, but Aries can be pushy while you prefer to float. It's fun—until someone gets impatient.",
        "communication_explanation": "Conversations are lively and never dull. Aries keeps things bold, and you keep things witty—just be careful not to talk over each other.",
        "emotional_explanation": "You move quickly through feelings, while Aries expects emotional fire. That mismatch can leave you both confused.",
        "intimacy_explanation": "The spark is there, playful and impulsive. But without emotional depth, it may feel more like a fling than a bond."
    },
    "Taurus": {
        "overall": 60,
        "communication": 70,
        "emotional": 50,
        "intimacy": 65,
        "overall_explanation": "Taurus wants steady, you want spontaneous. It can work—but it'll take patience neither of you is famous for.",
        "communication_explanation": "You love quick changes in topic; Taurus prefers calm, steady dialogue. You may find each other slow or scattered.",
        "emotional_explanation": "Taurus craves emotional consistency, while your moods change with the wind. That can feel destabilizing for them.",
        "intimacy_explanation": "Attraction might be there, but your playful energy might miss Taurus' need for sensual, slow-building closeness."
    },
    "Gemini": {
        "overall": 85,
        "communication": 95,
        "emotional": 70,
        "intimacy": 80,
        "overall_explanation": "Two Geminis together? You'll never run out of things to talk about—but you might both forget to come back down to earth.",
        "communication_explanation": "It's a ping-pong match of ideas, jokes, and constant chatter. You speak the same language and love every second of it.",
        "emotional_explanation": "You understand each other's emotional distance—and oddly, that brings a sense of safety.",
        "intimacy_explanation": "Light, playful, and full of surprises. Just don't expect either of you to lead with deep vulnerability without effort."
    },
    "Cancer": {
        "overall": 65,
        "communication": 70,
        "emotional": 75,
        "intimacy": 60,
        "overall_explanation": "You think your way through life, Cancer feels through it. You'll need to slow down—and they'll need to open up—to meet in the middle.",
        "communication_explanation": "You're quick and curious; Cancer is thoughtful and private. It takes time to learn how to really hear each other.",
        "emotional_explanation": "Cancer wants emotional depth, while you may dance around serious feelings. That gap can feel wide unless you're truly invested.",
        "intimacy_explanation": "It may start sweet, but Cancer wants soulful closeness. If you're not ready to dive in emotionally, they'll feel the disconnect."
    },
    "Leo": {
        "overall": 70,
        "communication": 80,
        "emotional": 65,
        "intimacy": 75,
        "overall_explanation": "You both shine bright and love attention, but Leo wants devotion while you need freedom. It's fun—but someone might get burned.",
        "communication_explanation": "Leo loves telling their story, and you're great at keeping things light and engaging. The banter is top-tier.",
        "emotional_explanation": "Leo wears their heart with pride, and you're more playful with yours. That difference can feel either exciting or mismatched.",
        "intimacy_explanation": "There's chemistry and charisma here. Just be sure it's not all sparkle and no depth—Leo needs to feel adored."
    },
    "Virgo": {
        "overall": 75,
        "communication": 85,
        "emotional": 70,
        "intimacy": 70,
        "overall_explanation": "You're both thinkers, but Virgo analyzes while you improvise. It's quirky and cerebral—if not always emotionally grounded.",
        "communication_explanation": "Words matter to both of you. Virgo keeps things precise, you keep things flowing—somehow, it works.",
        "emotional_explanation": "You're not the most sentimental pair, but there's mutual respect. Virgo's steady nature can help you stay emotionally anchored.",
        "intimacy_explanation": "The connection can be surprisingly sensual, but it's more mental than emotional unless you make space for vulnerability."
    },
    "Libra": {
        "overall": 80,
        "communication": 90,
        "emotional": 75,
        "intimacy": 80,
        "overall_explanation": "You click naturally—both love ideas, beauty, and charm. It's easy, breezy, and full of mental and emotional harmony.",
        "communication_explanation": "You share a love for words and connection. Conversations feel light yet deep, smart but never exhausting.",
        "emotional_explanation": "Libra helps you stay balanced, while you keep things exciting. It's emotionally comfortable—even if a little surface-level at times.",
        "intimacy_explanation": "Flirty, fun, and filled with mutual attraction. There's elegance in your connection that makes intimacy feel effortless."
    },
    "Scorpio": {
        "overall": 50,
        "communication": 55,
        "emotional": 60,
        "intimacy": 65,
        "overall_explanation": "You want freedom and lightness; Scorpio wants intensity and emotional depth. This can feel thrilling—or overwhelming.",
        "communication_explanation": "Scorpio speaks in subtext; you prefer a quick joke. If you're not careful, they'll see you as shallow, and you'll feel smothered.",
        "emotional_explanation": "Scorpio dives deep into emotions, while you skim the surface. That mismatch may leave both of you unsatisfied.",
        "intimacy_explanation": "There's physical intrigue, but emotional tension simmers underneath. It's powerful—but not always safe or sustainable."
    },
    "Sagittarius": {
        "overall": 80,
        "communication": 85,
        "emotional": 75,
        "intimacy": 80,
        "overall_explanation": "This is an exciting, wild ride. You both love freedom, fun, and new ideas—it's like finding your adventure twin.",
        "communication_explanation": "You're both enthusiastic and unfiltered—conversations flow fast and full of laughter, even during disagreements.",
        "emotional_explanation": "Neither of you clings emotionally, which brings ease—but you'll still need moments of real vulnerability to go deeper.",
        "intimacy_explanation": "Spontaneous, exciting, and full of play. Intimacy feels like an extension of your shared zest for life."
    },
    "Capricorn": {
        "overall": 55,
        "communication": 60,
        "emotional": 50,
        "intimacy": 60,
        "overall_explanation": "You're breezy, they're all business. It's not the easiest mix, but sometimes contrast brings clarity—if you're both open to it.",
        "communication_explanation": "Capricorn speaks with purpose, you speak with play. It can feel like you're speaking different dialects entirely.",
        "emotional_explanation": "You want fun, they want structure. Emotional expression may feel stiff to you, and too scattered for them.",
        "intimacy_explanation": "Capricorn can be sensual—but only if trust is built. Your lightheartedness may struggle to draw them out."
    },
    "Aquarius": {
        "overall": 85,
        "communication": 90,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "You both march to your own beat—and you love that about each other. It's an intellectually electric connection.",
        "communication_explanation": "Conversations are out-of-the-box and endlessly stimulating. You both thrive on ideas that break the rules.",
        "emotional_explanation": "There's emotional detachment on both sides—but it works. You feel safe being yourselves, even if you don't go super deep.",
        "intimacy_explanation": "Unique, open, and full of surprises. Intimacy here feels like an experiment in freedom and trust."
    },
    "Pisces": {
        "overall": 60,
        "communication": 65,
        "emotional": 70,
        "intimacy": 65,
        "overall_explanation": "Pisces is dreamy and sensitive; you're curious and quick. It's an odd mix that can feel sweet—or a bit ungrounded.",
        "communication_explanation": "You may find Pisces hard to pin down, and they may feel like you're always floating above the emotional stuff.",
        "emotional_explanation": "Pisces wants soul-level connection; you prefer to keep things light. You'll need to slow down and truly show up emotionally.",
        "intimacy_explanation": "There's potential for magic, but the pace has to match. Pisces craves depth, while you're often already on the next page."
    }
},
    "Cancer": {
    "Aries": {
        "overall": 60,
        "communication": 50,
        "emotional": 75,
        "intimacy": 65,
        "overall_explanation": "You lead with heart, Aries leads with fire. It can be exciting—but your emotional world may feel overlooked.",
        "communication_explanation": "You speak through emotion, they speak through action. Misunderstandings happen when neither slows down to truly listen.",
        "emotional_explanation": "You're ready to connect deeply, but Aries might not always meet you there. Their directness can sting if not softened.",
        "intimacy_explanation": "There's physical passion, but emotional safety may take longer. You'll need to feel held, not just touched."
    },
    "Taurus": {
        "overall": 85,
        "communication": 75,
        "emotional": 90,
        "intimacy": 80,
        "overall_explanation": "You both crave security, warmth, and real connection. This bond feels like coming home.",
        "communication_explanation": "You communicate with care, Taurus with calm. There's a mutual respect that makes you feel safe and seen.",
        "emotional_explanation": "Taurus gives you the emotional consistency you thrive on. In return, your warmth nourishes their quiet loyalty.",
        "intimacy_explanation": "Touch is tender, consistent, and meaningful. Intimacy feels natural—never rushed, always heartfelt."
    },
    "Gemini": {
        "overall": 65,
        "communication": 70,
        "emotional": 75,
        "intimacy": 60,
        "overall_explanation": "You lead with feeling, Gemini with thought. It's an odd match, but there's curiosity on both sides.",
        "communication_explanation": "Gemini keeps things light, while you often need depth. It takes patience to feel truly heard by each other.",
        "emotional_explanation": "You offer steady affection, they bring playful energy. It's sweet—until you need more than they're ready to give.",
        "intimacy_explanation": "There's fun and flirtation, but the emotional glue may be missing. You'll need trust to truly open up."
    },
    "Cancer": {
        "overall": 90,
        "communication": 85,
        "emotional": 95,
        "intimacy": 90,
        "overall_explanation": "You just get each other—emotionally, intuitively, and soulfully. This can feel like a connection that transcends words.",
        "communication_explanation": "You both speak the language of feelings. There's empathy in every word, even the unspoken ones.",
        "emotional_explanation": "You're both all-in emotionally. This bond runs deep, and you're not afraid to go there together.",
        "intimacy_explanation": "Intimacy feels sacred—more than physical. You create a safe space where vulnerability is welcomed, not feared."
    },
    "Leo": {
        "overall": 70,
        "communication": 65,
        "emotional": 80,
        "intimacy": 75,
        "overall_explanation": "You want emotional closeness; Leo wants admiration. It can work beautifully—or feel off-balance, depending on how love is expressed.",
        "communication_explanation": "Leo is bold, you're sensitive. You may retreat when they push too hard, unless they learn to speak your emotional language.",
        "emotional_explanation": "You give from the heart, and so does Leo—but they need to feel appreciated, and you need to feel emotionally held.",
        "intimacy_explanation": "There's passion here, but tenderness matters. When Leo slows down and you open up, the chemistry becomes real."
    },
    "Virgo": {
        "overall": 80,
        "communication": 80,
        "emotional": 85,
        "intimacy": 80,
        "overall_explanation": "This is a quietly nurturing match. Virgo brings you stability, and you show them how to feel deeply without fear.",
        "communication_explanation": "You both speak with care—Virgo with logic, you with emotion. Together, you find a beautiful middle ground.",
        "emotional_explanation": "You soften Virgo's edges, and they help organize your emotional world. You feel safe, understood, and appreciated.",
        "intimacy_explanation": "Steady, thoughtful, and deeply loving. This isn't flashy—it's soul-satisfying and sincere."
    },
    "Libra": {
        "overall": 75,
        "communication": 80,
        "emotional": 80,
        "intimacy": 75,
        "overall_explanation": "You both want peace and connection—but you seek it emotionally, while Libra seeks balance. It's gentle, though not always deep.",
        "communication_explanation": "Libra knows how to keep things smooth. You may wish they'd go deeper, but you appreciate their kindness.",
        "emotional_explanation": "You express your emotions freely, Libra more subtly. With mutual effort, you find a calm emotional rhythm.",
        "intimacy_explanation": "It's tender and romantic, even if a bit light. You might crave more depth, but the sweetness is undeniable."
    },
    "Scorpio": {
        "overall": 85,
        "communication": 80,
        "emotional": 90,
        "intimacy": 90,
        "overall_explanation": "This is a soulmate-level connection when it's right. You're both deep feelers, and neither of you plays love casually.",
        "communication_explanation": "You understand each other's silences. When you do speak, the words are powerful and often unspoken.",
        "emotional_explanation": "You both crave loyalty, depth, and emotional intensity. When you trust each other, it's an emotional fortress.",
        "intimacy_explanation": "Sensual, magnetic, and emotionally rich. It's more than physical—it's transformative when it clicks."
    },
    "Sagittarius": {
        "overall": 60,
        "communication": 65,
        "emotional": 55,
        "intimacy": 65,
        "overall_explanation": "You want roots, Sagittarius wants wings. The chemistry can be fun, but emotional needs might not align long-term.",
        "communication_explanation": "They joke when you need depth, and you may feel like your emotions are being brushed aside.",
        "emotional_explanation": "You need nurturing and closeness; they need space and freedom. It can feel like you're speaking two different hearts.",
        "intimacy_explanation": "There's attraction, but it may lack the emotional depth you desire. You want more than just a good time."
    },
    "Capricorn": {
        "overall": 75,
        "communication": 70,
        "emotional": 80,
        "intimacy": 75,
        "overall_explanation": "You're both loyal and value commitment—but while you lead with emotion, Capricorn leads with strategy. Together, you create balance.",
        "communication_explanation": "You speak with feeling, Capricorn with purpose. With patience, you learn to hear each other's language.",
        "emotional_explanation": "Capricorn may take time to open up, but once they do, you feel their depth. You bring warmth to their structure.",
        "intimacy_explanation": "There's tenderness beneath Capricorn's cool exterior. Your warmth draws it out, making intimacy feel earned and lasting."
    },
    "Aquarius": {
        "overall": 50,
        "communication": 55,
        "emotional": 50,
        "intimacy": 55,
        "overall_explanation": "You seek closeness, Aquarius seeks space. It's a tough dynamic that may leave you feeling emotionally adrift.",
        "communication_explanation": "Aquarius stays in their head, you stay in your heart. You may struggle to feel emotionally connected in conversation.",
        "emotional_explanation": "You want reassurance, they want independence. It's not impossible, but the emotional work is heavy.",
        "intimacy_explanation": "The connection may feel distant unless Aquarius truly shows up emotionally. Without that, it lacks the closeness you need."
    },
    "Pisces": {
        "overall": 90,
        "communication": 85,
        "emotional": 95,
        "intimacy": 90,
        "overall_explanation": "You and Pisces share a deep emotional world. This relationship feels intuitive, gentle, and profoundly nurturing.",
        "communication_explanation": "You both speak with emotion, intuition, and care. It's as if you understand each other without needing to explain.",
        "emotional_explanation": "This is emotional safety and soul-level connection. You both give selflessly, and it only deepens the love.",
        "intimacy_explanation": "Loving, sensual, and deeply soulful. When you're together, the outside world fades into the background."
    }
},
    "Leo": {
    "Aries": {
        "overall": 85,
        "communication": 75,
        "emotional": 70,
        "intimacy": 90,
        "overall_explanation": "You both thrive on passion, attention, and action. But when two alphas meet, someone has to learn to share the spotlight.",
        "communication_explanation": "Conversations are fiery and full of life—but if no one backs down, it can turn into a contest instead of a connection.",
        "emotional_explanation": "You express your emotions with flair; Aries does it with intensity. It's honest—but not always gentle.",
        "intimacy_explanation": "The chemistry is electric. There's fire, boldness, and a physical confidence that can make this truly unforgettable."
    },
    "Taurus": {
        "overall": 75,
        "communication": 70,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "You both value loyalty and sensuality, but Taurus is steady while you burn bright. You'll need to sync your emotional pacing.",
        "communication_explanation": "Taurus prefers calm and consistency; you bring drama and flair. With mutual patience, this becomes enriching rather than frustrating.",
        "emotional_explanation": "Taurus gives quietly, you give loudly. But the love runs deep on both sides—you just show it differently.",
        "intimacy_explanation": "This pairing can be steamy. You bring the heat, Taurus brings the depth—it's a grounded, luxurious kind of passion."
    },
    "Gemini": {
        "overall": 70,
        "communication": 80,
        "emotional": 65,
        "intimacy": 75,
        "overall_explanation": "Gemini keeps things light and clever; you want intensity and admiration. It's fun—but may lack emotional roots.",
        "communication_explanation": "You enjoy each other's wit and charm. Just don't mistake Gemini's detachment for disinterest—it's just their way.",
        "emotional_explanation": "You crave steady affection; they bounce between moods. You'll need to set the emotional tone if you want something real.",
        "intimacy_explanation": "It's playful, flirty, and exciting—but sometimes, you might feel like you're the only one investing emotionally."
    },
    "Cancer": {
        "overall": 70,
        "communication": 65,
        "emotional": 80,
        "intimacy": 75,
        "overall_explanation": "You love being adored, Cancer loves to nurture. It works—unless your fire scorches their sensitivity.",
        "communication_explanation": "You're bold and expressive; Cancer is quiet and emotional. You may have to soften your tone to truly connect.",
        "emotional_explanation": "You show love with flair; they show it through care. If you appreciate the difference, this becomes beautifully balanced.",
        "intimacy_explanation": "There's emotional warmth and steady passion here. Cancer brings the tenderness, you bring the spark."
    },
    "Leo": {
        "overall": 85,
        "communication": 80,
        "emotional": 85,
        "intimacy": 90,
        "overall_explanation": "This is a fiery, glamorous duo—full of pride, passion, and presence. You'll need to love each other's shine, not compete with it.",
        "communication_explanation": "You both love to be heard. Conversations sparkle, but someone has to listen, too.",
        "emotional_explanation": "You understand each other's highs and lows—and the need to be adored. Emotional expression comes naturally here.",
        "intimacy_explanation": "Bold, passionate, and confident. This is the kind of chemistry people write about—if egos don't get in the way."
    },
    "Virgo": {
        "overall": 60,
        "communication": 65,
        "emotional": 55,
        "intimacy": 65,
        "overall_explanation": "You live for the spotlight; Virgo prefers the sidelines. This contrast can be grounding—or just too different.",
        "communication_explanation": "Virgo is careful with words, you're bold with them. You may feel criticized, and they may feel overwhelmed.",
        "emotional_explanation": "You want open praise, Virgo shows love through quiet service. You'll need to read between the lines to feel fulfilled.",
        "intimacy_explanation": "There's attraction, but the emotional tones are offbeat. It may take effort for physical connection to feel truly intimate."
    },
    "Libra": {
        "overall": 80,
        "communication": 85,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "This is a beautiful, social, romantic pairing. You both adore attention—but Libra brings grace where you bring drama.",
        "communication_explanation": "Libra's charm smooths your fire. You feel admired, and they feel inspired—it's a natural give and take.",
        "emotional_explanation": "You both care deeply about being loved and appreciated. Emotional harmony is possible if you both feel seen.",
        "intimacy_explanation": "It's playful, magnetic, and luxurious. You bring heat, they bring finesse—and it blends beautifully."
    },
    "Scorpio": {
        "overall": 75,
        "communication": 70,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "You both love fiercely, but control and pride can get in the way. It's passionate, but power struggles are real.",
        "communication_explanation": "Scorpio is deep and intense; you're expressive and proud. You'll need to slow down and truly listen to each other.",
        "emotional_explanation": "There's loyalty and emotional depth on both sides, but neither of you likes to show weakness. Vulnerability is key.",
        "intimacy_explanation": "This connection runs hot. There's a magnetic pull here that can be healing—or consuming."
    },
    "Sagittarius": {
        "overall": 85,
        "communication": 80,
        "emotional": 80,
        "intimacy": 90,
        "overall_explanation": "This is a high-energy, passionate duo. You share a love for adventure, excitement, and boldness—it's a vibe that just clicks.",
        "communication_explanation": "You're both honest, playful, and open. Conversations flow, but watch for clashing opinions—neither of you backs down easily.",
        "emotional_explanation": "Sagittarius keeps things light, but you may want more affirmation. Still, the freedom you give each other creates real trust.",
        "intimacy_explanation": "This is fiery and uninhibited. Together, you turn intimacy into play—and play into something deeply satisfying."
    },
    "Capricorn": {
        "overall": 60,
        "communication": 55,
        "emotional": 60,
        "intimacy": 65,
        "overall_explanation": "Capricorn is grounded and cautious—you're expressive and bold. It can feel like you're living in separate realities.",
        "communication_explanation": "They get straight to the point, you need warmth and admiration. If they feel too cold, you might lose interest fast.",
        "emotional_explanation": "You crave praise, they crave practicality. There's care beneath the surface—but it's easy to miss without effort.",
        "intimacy_explanation": "Capricorn takes their time. You'll need to be patient and consistent if you want their passion to match yours."
    },
    "Aquarius": {
        "overall": 65,
        "communication": 70,
        "emotional": 60,
        "intimacy": 65,
        "overall_explanation": "You seek admiration; Aquarius seeks freedom. The chemistry is quirky and interesting—but emotional distance may leave you cold.",
        "communication_explanation": "You're expressive, Aquarius is cerebral. You might not always feel emotionally understood, even if they mean well.",
        "emotional_explanation": "You want to be adored and prioritized. Aquarius may feel too detached to give you the reassurance you need.",
        "intimacy_explanation": "There's intrigue and playfulness, but you may crave more intensity and consistency than Aquarius naturally offers."
    },
    "Pisces": {
        "overall": 70,
        "communication": 65,
        "emotional": 75,
        "intimacy": 70,
        "overall_explanation": "You bring fire, Pisces brings feeling. There's warmth here, but their sensitivity may clash with your boldness.",
        "communication_explanation": "You say things directly, Pisces may need more gentleness. It's a delicate balance between being honest and being kind.",
        "emotional_explanation": "Pisces is deeply emotional and giving, and you love to receive—but remember, they need tenderness in return.",
        "intimacy_explanation": "There's romance and softness here, but you might need to slow down to meet Pisces where they are emotionally."
    }
},
    "Virgo": {
    "Aries": {
        "overall": 55,
        "communication": 60,
        "emotional": 50,
        "intimacy": 60,
        "overall_explanation": "You prefer precision and planning, Aries prefers action without pause. This can be exciting—but also exhausting.",
        "communication_explanation": "You're thoughtful and clear, Aries is fast and bold. It can feel like you're solving two different puzzles at once.",
        "emotional_explanation": "You need consistency, Aries brings chaos. Unless you both slow down, emotions may get lost in translation.",
        "intimacy_explanation": "The spark is possible, but it needs grounding. You'll need to feel emotionally safe to truly let go."
    },
    "Taurus": {
        "overall": 80,
        "communication": 85,
        "emotional": 75,
        "intimacy": 80,
        "overall_explanation": "This is a stable, deeply compatible match. You both value loyalty, effort, and the beauty in small things.",
        "communication_explanation": "You speak in thoughtful, practical terms—Taurus listens with patience. There's a calm understanding between you.",
        "emotional_explanation": "You show love through care and actions, not drama—and Taurus loves you for it.",
        "intimacy_explanation": "Intimacy is slow, sensual, and respectful. Nothing rushed—everything earned."
    },
    "Gemini": {
        "overall": 75,
        "communication": 85,
        "emotional": 70,
        "intimacy": 70,
        "overall_explanation": "You're both sharp thinkers, but Gemini improvises where you plan. The mental connection is strong—if not always grounded.",
        "communication_explanation": "Your details meet their curiosity. You might clash over structure vs. spontaneity, but the dialogue never bores.",
        "emotional_explanation": "You want emotional reliability; they change moods like the wind. It's a challenge—but you're both adaptable.",
        "intimacy_explanation": "It's light and playful, with moments of depth. If trust builds, so does the connection."
    },
    "Cancer": {
        "overall": 80,
        "communication": 80,
        "emotional": 85,
        "intimacy": 80,
        "overall_explanation": "You bring the structure, Cancer brings the softness. Together, you create a deeply caring and balanced emotional space.",
        "communication_explanation": "You offer logic, Cancer offers empathy. It's a gentle flow that helps both of you grow.",
        "emotional_explanation": "You show love through action, they through emotion—and you both appreciate the other's loyalty.",
        "intimacy_explanation": "Tender, genuine, and nurturing. You build something steady that feels emotionally real."
    },
    "Leo": {
        "overall": 60,
        "communication": 65,
        "emotional": 55,
        "intimacy": 65,
        "overall_explanation": "Leo craves attention, you crave order. It's not impossible—but the emotional rhythm may never fully sync.",
        "communication_explanation": "Leo talks big, you focus on the details. It can feel like they're putting on a show while you're backstage organizing it.",
        "emotional_explanation": "You want practical devotion; they want praise and admiration. You'll need to stretch to meet in the middle.",
        "intimacy_explanation": "There can be chemistry, but it won't flourish unless Leo slows down and you open up emotionally."
    },
    "Virgo": {
        "overall": 85,
        "communication": 90,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "You speak the same language—quiet commitment, detail, and mutual support. It may not be flashy, but it's incredibly solid.",
        "communication_explanation": "You both communicate with precision and care. You know what the other needs without saying much.",
        "emotional_explanation": "You both tend to keep emotions controlled—but there's depth beneath the surface, and you respect that in each other.",
        "intimacy_explanation": "Thoughtful, respectful, and deeply fulfilling. It's a love built on trust, not theatrics."
    },
    "Libra": {
        "overall": 75,
        "communication": 85,
        "emotional": 75,
        "intimacy": 80,
        "overall_explanation": "You bring order, Libra brings grace. Together, you make something beautiful—if you don't get stuck in indecision.",
        "communication_explanation": "Libra's charm meets your clarity. You may differ in approach, but your mutual respect carries you through.",
        "emotional_explanation": "You both care deeply—but express it differently. You'll need to meet halfway to truly connect emotionally.",
        "intimacy_explanation": "There's elegance and gentleness in your physical connection. It may not be wild—but it feels safe and genuine."
    },
    "Scorpio": {
        "overall": 70,
        "communication": 75,
        "emotional": 75,
        "intimacy": 80,
        "overall_explanation": "You're both intense in your own ways—Scorpio emotionally, you mentally. Together, it can be surprisingly magnetic.",
        "communication_explanation": "Scorpio feels deeply; you analyze deeply. Conversations are layered, meaningful, and sometimes cryptic.",
        "emotional_explanation": "You both want trust and loyalty. Scorpio dives deeper, but your steadiness helps anchor them.",
        "intimacy_explanation": "There's quiet power here—slow-burning passion with intensity underneath. Intimacy is thoughtful, yet transformative."
    },
    "Sagittarius": {
        "overall": 55,
        "communication": 60,
        "emotional": 50,
        "intimacy": 60,
        "overall_explanation": "You love structure, Sagittarius loves freedom. It's hard to meet in the middle without compromise from both sides.",
        "communication_explanation": "You speak with precision; they jump from topic to topic. You may feel scattered, they may feel restricted.",
        "emotional_explanation": "You need reassurance and routine; they thrive on change. Emotional whiplash is a real risk here.",
        "intimacy_explanation": "There may be attraction, but it fades if you don't feel emotionally grounded and respected."
    },
    "Capricorn": {
        "overall": 80,
        "communication": 80,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "This is a high-functioning, grounded match. You both value growth, commitment, and steady love.",
        "communication_explanation": "You speak the same pragmatic, goal-oriented language. Conversations are productive and mutual.",
        "emotional_explanation": "Neither of you is overly expressive—but you both show up when it counts. That loyalty runs deep.",
        "intimacy_explanation": "Quiet passion, mutual respect, and a strong sense of timing. Intimacy deepens as trust grows."
    },
    "Aquarius": {
        "overall": 65,
        "communication": 70,
        "emotional": 60,
        "intimacy": 65,
        "overall_explanation": "You value order, Aquarius values freedom. You admire each other's minds—but emotional closeness may be harder to pin down.",
        "communication_explanation": "You're methodical, Aquarius is visionary. Ideas flow freely, but practical grounding is often missing.",
        "emotional_explanation": "You want structure in feelings; they resist labels. This emotional mismatch can leave you unsure where you stand.",
        "intimacy_explanation": "Curiosity can create sparks, but without emotional depth, the connection may feel inconsistent."
    },
    "Pisces": {
        "overall": 70,
        "communication": 65,
        "emotional": 75,
        "intimacy": 70,
        "overall_explanation": "You're the realist, Pisces the dreamer. There's compassion on both sides—but you may struggle to live in the same emotional world.",
        "communication_explanation": "You like facts, they speak in feelings. It's poetic—but frustrating if you crave clarity.",
        "emotional_explanation": "Pisces brings warmth and empathy; you bring stability. Together, you balance fantasy with function.",
        "intimacy_explanation": "It's sweet and affectionate—but only works if you can meet Pisces in their emotional depth without judgment."
    }
},
    "Libra": {
    "Aries": {
        "overall": 70,
        "communication": 80,
        "emotional": 65,
        "intimacy": 75,
        "overall_explanation": "You bring grace, Aries brings fire. This can be a passionate balance—or a clash of speed versus subtlety.",
        "communication_explanation": "You're diplomatic, Aries is direct. It can be a good balance if you don't get overwhelmed by their intensity.",
        "emotional_explanation": "You seek harmony, they seek action. You may feel rushed emotionally unless Aries slows down to really connect.",
        "intimacy_explanation": "There's attraction here, but intimacy blossoms when you both stop performing and let your guard down."
    },
    "Taurus": {
        "overall": 85,
        "communication": 90,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "You both love beauty, peace, and emotional steadiness. This connection is elegant, soft, and truly comforting.",
        "communication_explanation": "You understand each other's rhythms. Conversations flow naturally and rarely turn confrontational.",
        "emotional_explanation": "You both express affection through presence and gentleness. There's emotional ease here.",
        "intimacy_explanation": "Sensual, slow, and romantic—intimacy with Taurus feels like art you both create together."
    },
    "Gemini": {
        "overall": 80,
        "communication": 90,
        "emotional": 75,
        "intimacy": 80,
        "overall_explanation": "You both thrive on mental stimulation and social energy. This is a breezy, witty match full of charm.",
        "communication_explanation": "You love conversation, and so do they. Expect endless talking, laughter, and mental connection.",
        "emotional_explanation": "You may want more balance than they can always offer—but the emotional bond grows with shared experiences.",
        "intimacy_explanation": "Playful and fun with a touch of sophistication. You keep things light, yet still emotionally aware."
    },
    "Cancer": {
        "overall": 75,
        "communication": 80,
        "emotional": 80,
        "intimacy": 75,
        "overall_explanation": "You both care deeply, but in different ways—your charm meets Cancer's nurturing, creating a gentle blend of heart and mind.",
        "communication_explanation": "Cancer speaks emotionally, you speak with tact. With patience, your styles can truly complement each other.",
        "emotional_explanation": "You want peace, Cancer wants depth. If you can lean in instead of smoothing over, the connection becomes solid.",
        "intimacy_explanation": "Emotional and sensual, this match can be deeply fulfilling when both of you feel safe and prioritized."
    },
    "Leo": {
        "overall": 80,
        "communication": 85,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "You both adore romance, attention, and beauty. It's a dazzling pair—as long as you don't compete for the spotlight.",
        "communication_explanation": "You love flattery and finesse; Leo loves admiration. Together, words feel like poetry and praise.",
        "emotional_explanation": "You give your best when things feel fair and balanced—Leo brings warmth that makes you feel secure.",
        "intimacy_explanation": "Passionate, stylish, and emotionally alive. There's drama in the best way when love flows freely between you."
    },
    "Virgo": {
        "overall": 75,
        "communication": 85,
        "emotional": 75,
        "intimacy": 80,
        "overall_explanation": "Your charm meets Virgo's precision. It's a graceful pairing, especially when you appreciate each other's strengths.",
        "communication_explanation": "You bring tact, they bring clarity. You might want more poetry, they might want more order—but it works.",
        "emotional_explanation": "You both value subtlety and don't wear hearts on sleeves. That can feel calming—or too quiet, depending on your needs.",
        "intimacy_explanation": "Intimacy is refined, sensual, and emotionally respectful. You both take care in creating a meaningful connection."
    },
    "Libra": {
        "overall": 85,
        "communication": 95,
        "emotional": 85,
        "intimacy": 90,
        "overall_explanation": "Two Libras together can create something truly beautiful—harmonious, elegant, and emotionally graceful.",
        "communication_explanation": "You're fluent in charm and diplomacy. Conversations are thoughtful, romantic, and endlessly engaging.",
        "emotional_explanation": "You both avoid conflict and seek balance. While that brings peace, be careful not to avoid deeper truths.",
        "intimacy_explanation": "Romantic and visually pleasing—your intimacy is as much emotional as it is poetic and sensual."
    },
    "Scorpio": {
        "overall": 70,
        "communication": 75,
        "emotional": 80,
        "intimacy": 80,
        "overall_explanation": "You seek harmony, Scorpio seeks depth. If you can handle emotional intensity, this becomes a transformative match.",
        "communication_explanation": "You're light, Scorpio is intense. Honest talks require you to not retreat when things get heavy.",
        "emotional_explanation": "They want complete vulnerability—you prefer to keep peace. But when trust builds, so does emotional richness.",
        "intimacy_explanation": "There's intrigue and magnetism. If you're open to going deeper, intimacy becomes unforgettable."
    },
    "Sagittarius": {
        "overall": 75,
        "communication": 80,
        "emotional": 75,
        "intimacy": 80,
        "overall_explanation": "You love connection, they love freedom. It's fun, flirty, and full of energy—if you don't hold each other too tightly.",
        "communication_explanation": "You charm with balance, they entertain with truth. You both enjoy talking—but may dodge heavier topics.",
        "emotional_explanation": "You want togetherness, they want space. It works best when both of you feel emotionally independent yet close.",
        "intimacy_explanation": "Playful and passionate—this is a fun, exciting connection that keeps you both curious and lit up."
    },
    "Capricorn": {
        "overall": 70,
        "communication": 75,
        "emotional": 70,
        "intimacy": 75,
        "overall_explanation": "You want flow and beauty; Capricorn brings structure and substance. This can be grounding—or feel emotionally stiff.",
        "communication_explanation": "You bring charm, they bring purpose. Communication is respectful, but can lack spontaneity unless nurtured.",
        "emotional_explanation": "You want shared peace; they want results. Emotional expression may feel a bit formal—but it's sincere.",
        "intimacy_explanation": "Capricorn may not be as romantic as you, but they're steady. Over time, the intimacy becomes quietly strong."
    },
    "Aquarius": {
        "overall": 80,
        "communication": 85,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "You both think outside the box and love mental connection. This relationship feels modern, curious, and full of potential.",
        "communication_explanation": "You bring diplomacy, they bring innovation. Together, conversation never runs dry—and often surprises you both.",
        "emotional_explanation": "You care deeply, they care freely. The emotional tone is light, but there's real connection under the surface.",
        "intimacy_explanation": "It's unique, spontaneous, and creative. You both enjoy exploring love without pressure or predictability."
    },
    "Pisces": {
        "overall": 75,
        "communication": 70,
        "emotional": 80,
        "intimacy": 80,
        "overall_explanation": "You both dream of love in soft focus. If you're honest with each other, this can be a truly compassionate match.",
        "communication_explanation": "Pisces speaks with emotion, you with poise. It may take time, but eventually, you understand each other's rhythm.",
        "emotional_explanation": "You want peace, they want depth. It's emotionally rich—but you may need to address things instead of smoothing them over.",
        "intimacy_explanation": "There's romance, tenderness, and quiet beauty. You both treat love like art—and that's where the magic happens."
    }
},
    "Scorpio": {
    "Aries": {
        "overall": 65,
        "communication": 55,
        "emotional": 70,
        "intimacy": 80,
        "overall_explanation": "You're both passionate and driven, but your emotional depth can overwhelm Aries' need for quick action and independence.",
        "communication_explanation": "You communicate with emotional weight; Aries charges in with bluntness. It can lead to sparks—or silence.",
        "emotional_explanation": "You crave intensity and vulnerability; Aries prefers to stay in control. Unless they're willing to go deeper, you'll feel unmet.",
        "intimacy_explanation": "The chemistry is magnetic, but only fulfilling if Aries respects the emotional connection you need to feel truly close."
    },
    "Taurus": {
        "overall": 80,
        "communication": 70,
        "emotional": 85,
        "intimacy": 90,
        "overall_explanation": "This is a powerfully grounded match—slow, deep, and fiercely loyal. You both love with intensity and hold on tight.",
        "communication_explanation": "You speak through emotion; Taurus speaks through presence. Trust grows as each of you listens without judgment.",
        "emotional_explanation": "You both need emotional security, but you want it expressed. Taurus helps you feel safe without words.",
        "intimacy_explanation": "This is sensual, magnetic, and transformative. It's not just about touch—it's about soul-level connection."
    },
    "Gemini": {
        "overall": 50,
        "communication": 55,
        "emotional": 60,
        "intimacy": 65,
        "overall_explanation": "You crave emotional depth; Gemini wants lightness and change. Curiosity might draw you together—but it often doesn't last.",
        "communication_explanation": "You want truth and depth; Gemini talks in riddles and tangents. It can be stimulating—but also evasive.",
        "emotional_explanation": "You open emotionally with care; Gemini flutters in and out. That emotional inconsistency can feel unsafe to you.",
        "intimacy_explanation": "There may be initial intrigue, but without emotional commitment, it rarely becomes something truly satisfying."
    },
    "Cancer": {
        "overall": 85,
        "communication": 80,
        "emotional": 90,
        "intimacy": 90,
        "overall_explanation": "You both feel deeply and love intensely. This is a soulmate-level match when built on mutual trust and emotional safety.",
        "communication_explanation": "You intuitively understand each other. Even when you don't speak, there's an emotional language between you.",
        "emotional_explanation": "You both value emotional loyalty, vulnerability, and intimacy. This feels like home for both of you.",
        "intimacy_explanation": "Your connection is passionate and soulful. It's not just physical—it's emotionally sacred."
    },
    "Leo": {
        "overall": 75,
        "communication": 70,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "You're both strong, proud, and passionate—but power struggles can arise if no one's willing to give a little.",
        "communication_explanation": "Leo is expressive; you're intense. If pride doesn't get in the way, communication can be powerful and honest.",
        "emotional_explanation": "You both crave loyalty and admiration. The challenge is getting past defensiveness to access real intimacy.",
        "intimacy_explanation": "This is a fiery and magnetic connection. If mutual respect is present, intimacy becomes dramatic—in the best way."
    },
    "Virgo": {
        "overall": 70,
        "communication": 75,
        "emotional": 75,
        "intimacy": 80,
        "overall_explanation": "You bring depth, Virgo brings structure. If you trust each other, this becomes a thoughtful, emotionally rich pairing.",
        "communication_explanation": "You're emotional, they're analytical—but they listen well, and you appreciate their calm clarity.",
        "emotional_explanation": "You want full emotional presence; Virgo shows it in subtle ways. Still, their consistency earns your trust.",
        "intimacy_explanation": "There's passion here, but also care. Virgo's quiet intensity balances your emotional fire beautifully."
    },
    "Libra": {
        "overall": 70,
        "communication": 75,
        "emotional": 80,
        "intimacy": 80,
        "overall_explanation": "You go deep, Libra prefers balance. This can either be transformational—or frustrating if emotions get glossed over.",
        "communication_explanation": "You dig beneath the surface, Libra prefers harmony. If they avoid conflict, you might feel dismissed.",
        "emotional_explanation": "You crave raw connection; Libra wants emotional peace. When you both meet halfway, it becomes strong and elegant.",
        "intimacy_explanation": "There's intrigue, sensuality, and emotional charge. Libra brings light, you bring depth—together, it's magnetic."
    },
    "Scorpio": {
        "overall": 90,
        "communication": 85,
        "emotional": 95,
        "intimacy": 95,
        "overall_explanation": "Two Scorpios together? This is deep, devoted, and emotionally all-consuming—for better or worse.",
        "communication_explanation": "You both speak through intensity. If you let down your guards, communication becomes raw and real.",
        "emotional_explanation": "You feel everything, and so do they. When trust is built, this is emotional intimacy at its most profound.",
        "intimacy_explanation": "Soulful, seductive, and powerful. The connection is almost telepathic—intimacy becomes spiritual."
    },
    "Sagittarius": {
        "overall": 65,
        "communication": 70,
        "emotional": 65,
        "intimacy": 70,
        "overall_explanation": "You want emotional depth; Sagittarius wants freedom. The tension between the two can be exciting—but unstable.",
        "communication_explanation": "Sagittarius brings humor, you bring weight. It can be refreshing—or frustrating if you feel they're dodging your truths.",
        "emotional_explanation": "You need consistency; they thrive on movement. Emotional security may feel out of reach without serious effort.",
        "intimacy_explanation": "It's adventurous and bold—but unless emotions deepen, you may feel like something's missing."
    },
    "Capricorn": {
        "overall": 80,
        "communication": 75,
        "emotional": 85,
        "intimacy": 85,
        "overall_explanation": "You both value loyalty, power, and emotional privacy. This relationship feels solid, serious, and worth the investment.",
        "communication_explanation": "You speak from the heart, Capricorn speaks with strategy. But there's mutual respect in every word.",
        "emotional_explanation": "You both protect your emotions fiercely. Over time, vulnerability becomes a shared strength rather than a weakness.",
        "intimacy_explanation": "When trust is earned, the connection is magnetic and quietly intense. Intimacy grows deeper with time."
    },
    "Aquarius": {
        "overall": 55,
        "communication": 60,
        "emotional": 50,
        "intimacy": 55,
        "overall_explanation": "You crave soul-deep intimacy; Aquarius often stays in their head. It's a challenge to connect unless they open emotionally.",
        "communication_explanation": "You want emotional truths; Aquarius wants abstract ideas. You may feel like they're never fully *with* you.",
        "emotional_explanation": "You need emotional consistency, they need independence. The emotional tone often feels mismatched.",
        "intimacy_explanation": "There may be curiosity, but real closeness requires more than intellectual stimulation. You need heart—not just mind."
    },
    "Pisces": {
        "overall": 85,
        "communication": 80,
        "emotional": 90,
        "intimacy": 90,
        "overall_explanation": "This is a deeply emotional and intuitive bond. You both understand love through feeling, not words.",
        "communication_explanation": "You feel each other without needing to explain everything. There's an emotional language only you two speak.",
        "emotional_explanation": "You both need trust, depth, and a safe emotional space. Together, you build that naturally.",
        "intimacy_explanation": "Sensual, healing, and spiritually connected. This intimacy feels like a quiet universe you both get lost in."
    }
},
    "Sagittarius": {
    "Aries": {
        "overall": 90,
        "communication": 80,
        "emotional": 75,
        "intimacy": 85,
        "overall_explanation": "This is a bold, adventurous duo. You both crave freedom, excitement, and new experiences—it's pure fire and movement.",
        "communication_explanation": "You speak the same energetic language. There's little drama, just straight-shooting honesty and shared laughter.",
        "emotional_explanation": "You both like to keep things light, but there's a quiet emotional loyalty that forms when neither of you feels pinned down.",
        "intimacy_explanation": "Playful, passionate, and spontaneous—your chemistry never stays still, and that's exactly how you like it."
    },
    "Taurus": {
        "overall": 60,
        "communication": 65,
        "emotional": 55,
        "intimacy": 70,
        "overall_explanation": "You want freedom; Taurus wants predictability. There's affection, but your rhythms can feel worlds apart.",
        "communication_explanation": "You bounce from idea to idea; Taurus prefers slower, more grounded conversations. That gap can be frustrating.",
        "emotional_explanation": "Taurus craves consistency, and you're constantly in motion. Your heart may be in it—but your timing may be off.",
        "intimacy_explanation": "There's physical warmth here, but it may lack the emotional resonance Taurus needs to feel truly secure."
    },
    "Gemini": {
        "overall": 80,
        "communication": 85,
        "emotional": 75,
        "intimacy": 80,
        "overall_explanation": "This is a fun, curious, and endlessly dynamic match. You both crave variety, stimulation, and a love that feels alive.",
        "communication_explanation": "You thrive on shared ideas and witty banter. Every conversation feels like a new adventure.",
        "emotional_explanation": "Neither of you gets too heavy, but there's a shared emotional optimism that makes this feel easy and real.",
        "intimacy_explanation": "Fun, flirtatious, and full of surprises—you explore each other like an open book with extra chapters."
    },
    "Cancer": {
        "overall": 60,
        "communication": 65,
        "emotional": 55,
        "intimacy": 65,
        "overall_explanation": "Cancer wants emotional safety; you want wide-open skies. This can feel like comfort vs. chaos unless handled gently.",
        "communication_explanation": "You're upbeat and direct; Cancer is soft and cautious. They may feel hurt while you feel misunderstood.",
        "emotional_explanation": "You seek adventure, they seek reassurance. With effort, you might meet halfway—but it's rarely effortless.",
        "intimacy_explanation": "The connection may be sweet at first, but emotional mismatches can make it hard to sustain long-term closeness."
    },
    "Leo": {
        "overall": 85,
        "communication": 80,
        "emotional": 80,
        "intimacy": 90,
        "overall_explanation": "There's excitement, heat, and a sense of endless possibility. You lift each other up—and never hold each other back.",
        "communication_explanation": "You both love being heard and appreciated. Conversations are fun, confident, and never short on passion.",
        "emotional_explanation": "Leo brings heart, you bring perspective. Together, you create a fiery yet surprisingly stable emotional rhythm.",
        "intimacy_explanation": "Magnetic, bold, and adventurous—intimacy feels like play, passion, and connection all in one."
    },
    "Virgo": {
        "overall": 55,
        "communication": 60,
        "emotional": 50,
        "intimacy": 60,
        "overall_explanation": "Virgo wants order, you want spontaneity. Unless you both adapt, it can feel like speaking two different love languages.",
        "communication_explanation": "You're casual and spontaneous; Virgo prefers structure and clarity. Misunderstandings come quickly if patience runs low.",
        "emotional_explanation": "You may avoid emotional heaviness, while Virgo analyzes every feeling. That contrast can create distance.",
        "intimacy_explanation": "There's curiosity, but not always comfort. It takes emotional effort to truly feel connected here."
    },
    "Libra": {
        "overall": 75,
        "communication": 80,
        "emotional": 75,
        "intimacy": 80,
        "overall_explanation": "Libra brings charm, you bring excitement. It's a graceful yet lively mix of romance, fun, and curiosity.",
        "communication_explanation": "You love freedom, they love harmony. Conversations are smooth, flirty, and full of playful tension.",
        "emotional_explanation": "You both like to keep things light but meaningful. It's a gentle emotional match that feels comfortable.",
        "intimacy_explanation": "Fun, balanced, and sensually charged. It's an easy and beautiful space to explore desire together."
    },
    "Scorpio": {
        "overall": 65,
        "communication": 70,
        "emotional": 65,
        "intimacy": 70,
        "overall_explanation": "You value freedom, Scorpio values depth. There's intrigue here—but also emotional tension if trust is shaky.",
        "communication_explanation": "You keep things light; they crave substance. If you stay open, their intensity can ground your energy.",
        "emotional_explanation": "You run from emotional heaviness, they live in it. It's possible to meet halfway, but it won't come naturally.",
        "intimacy_explanation": "Passion exists, but emotional pacing may clash. You want space; they want surrender."
    },
    "Sagittarius": {
        "overall": 90,
        "communication": 85,
        "emotional": 80,
        "intimacy": 90,
        "overall_explanation": "This is a match made for freedom, laughter, and unshakable optimism. You see the world the same—and you run toward it together.",
        "communication_explanation": "You both talk fast, dream big, and never tire of learning from each other. Conversations are endless and energizing.",
        "emotional_explanation": "You understand each other's emotional independence and don't need constant reassurance to feel loved.",
        "intimacy_explanation": "Adventurous, passionate, and full of chemistry. You keep each other on your toes—and in each other's arms."
    },
    "Capricorn": {
        "overall": 60,
        "communication": 55,
        "emotional": 60,
        "intimacy": 65,
        "overall_explanation": "Capricorn builds slowly, you leap freely. It can feel like a tug-of-war between spontaneity and structure.",
        "communication_explanation": "You're blunt and humorous; they're cautious and serious. The disconnect is real unless both are willing to stretch.",
        "emotional_explanation": "You avoid emotional heaviness; Capricorn keeps it bottled. Vulnerability might always feel slightly out of reach.",
        "intimacy_explanation": "There can be quiet passion here, but it needs effort. You want fun; they want depth—ideally, you learn to offer both."
    },
    "Aquarius": {
        "overall": 80,
        "communication": 85,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "You both thrive on freedom, ideas, and adventure. This is a mental and emotional match that keeps you both inspired.",
        "communication_explanation": "Talks are full of insights, dreams, and spontaneous tangents. You both love where the conversation goes.",
        "emotional_explanation": "You understand each other's emotional independence and respect personal space—it's a low-drama, high-trust vibe.",
        "intimacy_explanation": "Innovative, playful, and satisfying. You explore each other with openness and a shared sense of curiosity."
    },
    "Pisces": {
        "overall": 70,
        "communication": 65,
        "emotional": 75,
        "intimacy": 75,
        "overall_explanation": "Pisces brings softness, you bring fire. It's a soulful adventure—if you don't trample their sensitivity along the way.",
        "communication_explanation": "You speak freely; Pisces speaks in feelings. Misunderstandings happen unless you slow down and really tune in.",
        "emotional_explanation": "They need reassurance; you need room to breathe. Still, their compassion touches you in unexpected ways.",
        "intimacy_explanation": "There's sweetness, passion, and a poetic edge. If trust builds, intimacy becomes something truly beautiful."
    }
},
    "Capricorn": {
    "Aries": {
        "overall": 50,
        "communication": 45,
        "emotional": 55,
        "intimacy": 60,
        "overall_explanation": "You value structure and caution; Aries thrives on spontaneity. While there's respect, the energy can feel mismatched.",
        "communication_explanation": "You choose your words carefully, Aries moves fast. Patience runs thin if neither of you slows down to meet in the middle.",
        "emotional_explanation": "You're emotionally reserved, they're direct and fiery. That contrast can leave you feeling exposed—or them, ignored.",
        "intimacy_explanation": "There's potential for grounded chemistry, but real connection needs time and emotional openness from both sides."
    },
    "Taurus": {
        "overall": 90,
        "communication": 80,
        "emotional": 85,
        "intimacy": 90,
        "overall_explanation": "This is a rock-solid bond. You both value loyalty, security, and building something meaningful together.",
        "communication_explanation": "You speak the same language—calm, clear, and intentional. Conversations feel productive and grounding.",
        "emotional_explanation": "You both open slowly but deeply. There's safety in the way your emotional rhythms align.",
        "intimacy_explanation": "Trust runs deep here. Your physical and emotional intimacy grows naturally, and lasts."
    },
    "Gemini": {
        "overall": 55,
        "communication": 60,
        "emotional": 50,
        "intimacy": 60,
        "overall_explanation": "You want stability, Gemini wants flexibility. There's curiosity, but your needs often travel in different directions.",
        "communication_explanation": "Gemini talks fast and loose, you choose your words. Misunderstandings happen when speed overrides substance.",
        "emotional_explanation": "You need reliability to feel safe. Gemini may feel emotionally distant or inconsistent to you.",
        "intimacy_explanation": "There might be chemistry, but consistency is missing. Without emotional alignment, it stays surface-level."
    },
    "Cancer": {
        "overall": 75,
        "communication": 70,
        "emotional": 80,
        "intimacy": 75,
        "overall_explanation": "You balance each other beautifully—you're steady, they're nurturing. Together, you build lasting emotional safety.",
        "communication_explanation": "You're both reserved at first, but there's mutual care in how you choose your words.",
        "emotional_explanation": "You open up through action, Cancer through feeling. When you respect those styles, emotional depth flourishes.",
        "intimacy_explanation": "This is slow-burning and tender. It becomes deeply fulfilling when emotional trust is built."
    },
    "Leo": {
        "overall": 60,
        "communication": 55,
        "emotional": 60,
        "intimacy": 65,
        "overall_explanation": "Leo wants to shine; you want results. If egos clash, it's tough—but if aligned, this can be a powerful pair.",
        "communication_explanation": "Leo expresses boldly, you stay composed. It may feel like you're in different theaters, speaking different scripts.",
        "emotional_explanation": "You take your time emotionally; Leo wants warmth and attention. That can lead to unmet needs on both sides.",
        "intimacy_explanation": "There's strong attraction, but intimacy only deepens when both are willing to step out of their comfort zones."
    },
    "Virgo": {
        "overall": 80,
        "communication": 80,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "You're a power couple in the making. Detail-focused, loyal, and grounded—this is love built to last.",
        "communication_explanation": "Clear, calm, and thoughtful—your talks are efficient but meaningful, with little drama.",
        "emotional_explanation": "You understand each other's quiet emotional worlds. There's respect and tenderness underneath the practicality.",
        "intimacy_explanation": "There's a shared appreciation for depth, patience, and presence. This is intimacy that matures beautifully."
    },
    "Libra": {
        "overall": 70,
        "communication": 75,
        "emotional": 70,
        "intimacy": 75,
        "overall_explanation": "Libra seeks beauty, you seek results. If your values align, this can be a surprisingly balanced and graceful match.",
        "communication_explanation": "Libra brings charm, you bring focus. You may clash on pace, but mutual respect keeps it steady.",
        "emotional_explanation": "You may seem too reserved for Libra's romanticism—but once grounded, you both bring out a softer side in each other.",
        "intimacy_explanation": "When trust is built, this becomes quietly passionate. It's a slower burn—but one that lasts."
    },
    "Scorpio": {
        "overall": 80,
        "communication": 75,
        "emotional": 85,
        "intimacy": 85,
        "overall_explanation": "You both value loyalty, privacy, and emotional depth. It's an intense, grounded match built on mutual trust.",
        "communication_explanation": "You both speak with intention. There's often more said between the lines than out loud—and that works for both of you.",
        "emotional_explanation": "You both protect your hearts—but when you open, it's real and unwavering. Emotional loyalty is your glue.",
        "intimacy_explanation": "This is passionate and private. The intimacy feels safe, magnetic, and powerful."
    },
    "Sagittarius": {
        "overall": 60,
        "communication": 55,
        "emotional": 60,
        "intimacy": 65,
        "overall_explanation": "You want to plan, they want to explore. There's affection here, but your styles often pull in opposite directions.",
        "communication_explanation": "You're focused and grounded; Sagittarius prefers spontaneity and humor. You may miss each other's meaning.",
        "emotional_explanation": "You crave consistency; they crave movement. Unless you compromise, emotions may never fully sync.",
        "intimacy_explanation": "Fun and attraction are possible, but deep connection requires more vulnerability than either may show at first."
    },
    "Capricorn": {
        "overall": 90,
        "communication": 85,
        "emotional": 85,
        "intimacy": 90,
        "overall_explanation": "You both understand what it means to build a life with intention. Together, you're grounded, loyal, and unstoppable.",
        "communication_explanation": "You speak the same language—direct, honest, and with purpose. Conversations are productive and respectful.",
        "emotional_explanation": "You're both slow to open, but deeply loyal once you do. There's mutual trust in your emotional restraint.",
        "intimacy_explanation": "It's subtle, strong, and deeply satisfying. This is a bond that gets better over time."
    },
    "Aquarius": {
        "overall": 70,
        "communication": 75,
        "emotional": 70,
        "intimacy": 75,
        "overall_explanation": "You bring structure, they bring vision. It's unconventional, but with shared respect, this can work in surprising ways.",
        "communication_explanation": "You're practical, they're abstract—but both of you enjoy meaningful, big-picture conversations.",
        "emotional_explanation": "You may hold back while they detach—but when connected, there's a unique emotional honesty between you.",
        "intimacy_explanation": "It may not be traditionally romantic, but it's stimulating, free, and emotionally sincere when grounded in trust."
    },
    "Pisces": {
        "overall": 75,
        "communication": 70,
        "emotional": 80,
        "intimacy": 80,
        "overall_explanation": "You're grounded, Pisces is dreamy. If you meet halfway, this can be a beautiful balance of vision and reality.",
        "communication_explanation": "Pisces speaks in feelings, you speak in facts. The challenge is finding emotional clarity without losing patience.",
        "emotional_explanation": "You're protective, they're vulnerable. When you soften and they ground, you nurture each other beautifully.",
        "intimacy_explanation": "Pisces brings tenderness to your strength. Together, intimacy becomes soulful and enduring."
    }
},
    "Aquarius": {
    "Aries": {
        "overall": 75,
        "communication": 80,
        "emotional": 65,
        "intimacy": 70,
        "overall_explanation": "You both love freedom and fresh ideas, but your emotional rhythms may feel slightly out of sync.",
        "communication_explanation": "You're both quick thinkers and direct speakers—this creates exciting, fast-moving conversations.",
        "emotional_explanation": "Aries wears emotions boldly; you often stay cool and reserved. This can lead to frustration if left unchecked.",
        "intimacy_explanation": "The spark is definitely there, but emotional depth might require effort on your part to fully connect."
    },
    "Taurus": {
        "overall": 50,
        "communication": 60,
        "emotional": 45,
        "intimacy": 55,
        "overall_explanation": "Taurus wants closeness and routine, you need space and unpredictability. It's a challenging fit unless you're both highly flexible.",
        "communication_explanation": "Taurus likes steady, grounded talks; your mind leaps ahead. It's easy to feel like you're not speaking the same language.",
        "emotional_explanation": "They offer consistent warmth, while you may seem emotionally detached. That contrast can feel lonely to both.",
        "intimacy_explanation": "There's attraction, but intimacy can feel lopsided unless you're willing to meet Taurus in the middle emotionally."
    },
    "Gemini": {
        "overall": 85,
        "communication": 90,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "You're both mentally curious and value freedom—this is a vibrant, electric connection where ideas and excitement never run dry.",
        "communication_explanation": "You talk about everything and anything. It's fast, fun, and full of imagination.",
        "emotional_explanation": "Neither of you gets too heavy, and that makes emotional connection feel safe and comfortable.",
        "intimacy_explanation": "Playful, clever, and experimental—there's a unique chemistry that keeps evolving with time."
    },
    "Cancer": {
        "overall": 50,
        "communication": 55,
        "emotional": 50,
        "intimacy": 55,
        "overall_explanation": "Cancer wants emotional closeness; you want space and mental connection. It takes serious compromise to bridge this gap.",
        "communication_explanation": "Cancer speaks from the heart; you speak from the mind. Misunderstandings can easily arise if empathy is lacking.",
        "emotional_explanation": "You tend to detach, while Cancer clings. Unless there's balance, one of you will always feel left behind.",
        "intimacy_explanation": "Physical closeness may happen, but emotional vulnerability will be the real challenge in this pairing."
    },
    "Leo": {
        "overall": 65,
        "communication": 70,
        "emotional": 60,
        "intimacy": 65,
        "overall_explanation": "Leo wants to be adored; you want to feel free. This can feel like a push-pull dynamic without mutual admiration.",
        "communication_explanation": "Your quirky mind excites Leo, but your emotional coolness might confuse them.",
        "emotional_explanation": "You're emotionally independent; Leo wants warmth and attention. That difference can create distance if not managed.",
        "intimacy_explanation": "There's passion, but also ego clashes. You'll need to work together to balance desire with respect for each other's pace."
    },
    "Virgo": {
        "overall": 65,
        "communication": 70,
        "emotional": 60,
        "intimacy": 65,
        "overall_explanation": "You're both thinkers, but Virgo's need for structure can clash with your free-form nature. Still, respect can build something solid.",
        "communication_explanation": "You both enjoy analyzing life, though Virgo prefers order where you see patterns in chaos.",
        "emotional_explanation": "Virgo wants clarity and stability; you keep things fluid and abstract. That can lead to missed emotional cues.",
        "intimacy_explanation": "There's potential here if you both let go of control and allow the connection to deepen naturally."
    },
    "Libra": {
        "overall": 80,
        "communication": 85,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "You're both airy, social, and idealistic—there's a graceful flow here that feels fresh, open, and full of possibility.",
        "communication_explanation": "You vibe on the same intellectual wavelength. Conversations are stimulating, elegant, and often inspiring.",
        "emotional_explanation": "Libra brings charm, you bring originality. Emotionally, you create a light but meaningful connection.",
        "intimacy_explanation": "There's beauty, play, and intellectual intimacy. It feels effortless and emotionally safe for both of you."
    },
    "Scorpio": {
        "overall": 55,
        "communication": 60,
        "emotional": 50,
        "intimacy": 55,
        "overall_explanation": "Scorpio craves emotional depth; you crave space and objectivity. This can quickly become a game of push and pull.",
        "communication_explanation": "You stay logical; Scorpio gets intense. It's hard to find common ground unless you both shift your approach.",
        "emotional_explanation": "They seek emotional fusion; you maintain personal distance. That dynamic can leave one or both of you feeling misunderstood.",
        "intimacy_explanation": "Attraction exists, but vulnerability may feel mismatched. True closeness will take patience—and lots of trust."
    },
    "Sagittarius": {
        "overall": 80,
        "communication": 85,
        "emotional": 80,
        "intimacy": 85,
        "overall_explanation": "You're both free spirits with big ideas and open hearts. This is a connection that thrives on adventure and originality.",
        "communication_explanation": "You bounce ideas off each other with ease—it's upbeat, clever, and endlessly engaging.",
        "emotional_explanation": "You both value emotional independence. There's trust here without pressure, and that feels liberating.",
        "intimacy_explanation": "Intimacy feels like exploration. You're curious, open, and mutually respectful in how you show affection."
    },
    "Capricorn": {
        "overall": 70,
        "communication": 75,
        "emotional": 70,
        "intimacy": 75,
        "overall_explanation": "Capricorn brings structure, you bring innovation. It's unconventional, but you can learn from each other if mutual respect is strong.",
        "communication_explanation": "You're future-focused and abstract; Capricorn is grounded and methodical. You both listen and challenge each other in healthy ways.",
        "emotional_explanation": "You tend to detach; Capricorn tends to contain. While both of you are private, you understand each other's emotional restraint.",
        "intimacy_explanation": "Not overly romantic, but quietly deep. This is a connection that thrives when built on trust and shared goals."
    },
    "Aquarius": {
        "overall": 85,
        "communication": 90,
        "emotional": 85,
        "intimacy": 90,
        "overall_explanation": "You've met your match in independence and originality. This is a relationship of mutual freedom, ideas, and deep mutual respect.",
        "communication_explanation": "You both love exploring the weird, the wild, and the intellectual. Words flow effortlessly here.",
        "emotional_explanation": "There's emotional understanding without pressure—space is respected, yet connection feels real.",
        "intimacy_explanation": "This is intimacy without convention. It's electric, authentic, and uniquely yours."
    },
    "Pisces": {
        "overall": 70,
        "communication": 65,
        "emotional": 75,
        "intimacy": 75,
        "overall_explanation": "Pisces brings empathy and softness, you bring vision and originality. If you respect each other's differences, the connection can be beautifully strange.",
        "communication_explanation": "You're detached and abstract; Pisces is poetic and emotional. It's quirky—but can be touching if both listen with care.",
        "emotional_explanation": "Pisces offers emotional openness you don't always know how to receive—but their compassion touches you deeply.",
        "intimacy_explanation": "This connection is dreamy and unconventional. It can feel otherworldly when hearts are aligned."
    }
},
    "Pisces": {
    "Aries": {
        "overall": 60,
        "communication": 55,
        "emotional": 70,
        "intimacy": 65,
        "overall_explanation": "Your deep emotions can feel exposed under Aries' bluntness, but there's shared warmth if patience is shown.",
        "communication_explanation": "Aries is bold and fast; you're gentle and intuitive. Misunderstandings can arise unless both of you slow down.",
        "emotional_explanation": "You feel things deeply, while Aries may rush past emotional nuance. That can sting unless they learn to pause with you.",
        "intimacy_explanation": "There's attraction, but you might crave more tenderness than Aries naturally offers. With care, it can bloom beautifully."
    },
    "Taurus": {
        "overall": 70,
        "communication": 65,
        "emotional": 80,
        "intimacy": 75,
        "overall_explanation": "You both seek connection and emotional safety—Taurus gives you the steady ground you need to trust.",
        "communication_explanation": "You speak in feelings; Taurus speaks in actions. Together, that can create a lovely and grounding rhythm.",
        "emotional_explanation": "Taurus offers stability, you offer compassion. Emotionally, you soothe each other.",
        "intimacy_explanation": "It's gentle, sensual, and warm—like a slow dance you never want to end."
    },
    "Gemini": {
        "overall": 60,
        "communication": 65,
        "emotional": 70,
        "intimacy": 65,
        "overall_explanation": "Gemini brings fun and ideas, but you may long for deeper emotional grounding. It's lighthearted, but may feel fleeting.",
        "communication_explanation": "You speak from the heart; Gemini speaks from the head. It's playful, but emotional cues can get lost.",
        "emotional_explanation": "You crave depth; Gemini prefers variety. There's care here, but not always consistency.",
        "intimacy_explanation": "It may start with curiosity, but needs emotional vulnerability to truly satisfy you."
    },
    "Cancer": {
        "overall": 90,
        "communication": 85,
        "emotional": 95,
        "intimacy": 90,
        "overall_explanation": "You and Cancer speak the same emotional language. This is a nurturing, intuitive, and safe space for love to thrive.",
        "communication_explanation": "You just *get* each other. Feelings are shared without needing too many words.",
        "emotional_explanation": "Your bond runs deep. Empathy flows both ways, creating a beautiful emotional sanctuary.",
        "intimacy_explanation": "It's soft, soulful, and beautifully intimate—like coming home to each other again and again."
    },
    "Leo": {
        "overall": 70,
        "communication": 65,
        "emotional": 75,
        "intimacy": 70,
        "overall_explanation": "Leo's boldness can overwhelm your sensitivity, but their warmth is also comforting when it comes from the heart.",
        "communication_explanation": "Leo speaks with confidence; you speak with nuance. Bridging that gap requires mutual curiosity.",
        "emotional_explanation": "You feel deeply, while Leo radiates energy. If they slow down, and you open up, the connection can deepen beautifully.",
        "intimacy_explanation": "There's heat and heart here, but it only works if Leo offers gentleness and you offer confidence."
    },
    "Virgo": {
        "overall": 70,
        "communication": 65,
        "emotional": 75,
        "intimacy": 70,
        "overall_explanation": "Virgo offers grounding, you offer emotional richness. You may see the world differently—but you can complement each other well.",
        "communication_explanation": "You speak emotionally; Virgo speaks practically. You'll need to meet in the middle to be heard.",
        "emotional_explanation": "Virgo can help you find emotional clarity, while you soften their edges with compassion.",
        "intimacy_explanation": "It may not be flashy, but there's real tenderness if both of you feel emotionally secure."
    },
    "Libra": {
        "overall": 75,
        "communication": 70,
        "emotional": 80,
        "intimacy": 80,
        "overall_explanation": "You both crave connection and beauty, though your emotional needs might pull in different directions at times.",
        "communication_explanation": "Libra keeps things light; you go deep. The challenge is balancing charm with vulnerability.",
        "emotional_explanation": "You feel fully, Libra prefers balance. But there's real care and sweetness between you.",
        "intimacy_explanation": "It's dreamy and romantic. When it's good, it feels like a fairytale you're writing together."
    },
    "Scorpio": {
        "overall": 85,
        "communication": 80,
        "emotional": 90,
        "intimacy": 90,
        "overall_explanation": "You both feel deeply and intuitively, creating an emotionally rich and transformative bond that runs beneath the surface.",
        "communication_explanation": "Words aren't always needed—you read each other emotionally, even in silence.",
        "emotional_explanation": "Your shared intensity creates a powerful emotional world. Vulnerability here feels safe, even sacred.",
        "intimacy_explanation": "It's passionate, soulful, and magnetic. You both crave deep emotional fusion—and you find it here."
    },
    "Sagittarius": {
        "overall": 70,
        "communication": 65,
        "emotional": 75,
        "intimacy": 75,
        "overall_explanation": "Sagittarius brings energy and optimism, but their bluntness can clash with your emotional sensitivity. Still, there's warmth if mutual respect is present.",
        "communication_explanation": "You're subtle; they're direct. It can feel jarring, but also refreshing when approached with openness.",
        "emotional_explanation": "You crave connection; they crave space. Balance comes when neither feels smothered or ignored.",
        "intimacy_explanation": "It's playful and surprising. With trust, it can turn into a deep and joyful bond."
    },
    "Capricorn": {
        "overall": 75,
        "communication": 70,
        "emotional": 80,
        "intimacy": 80,
        "overall_explanation": "Capricorn gives you the safety to let your emotions flow. You bring softness to their structure. It's a beautiful balance of earth and water.",
        "communication_explanation": "Capricorn is clear and steady; you're poetic and emotional. Together, you learn to bridge logic and feeling.",
        "emotional_explanation": "You feel everything; they build strong foundations. You bring them closer to their heart, and they help you feel protected.",
        "intimacy_explanation": "It's slower-burning, but worth the wait. Once trust is earned, the connection runs deep and steady."
    },
    "Aquarius": {
        "overall": 70,
        "communication": 65,
        "emotional": 75,
        "intimacy": 75,
        "overall_explanation": "Aquarius can feel distant to your emotional depth, but you're both kind and imaginative—this relationship can thrive if you respect each other's differences.",
        "communication_explanation": "They think in ideas, you think in feelings. It's a challenge—but one that can create a beautiful contrast.",
        "emotional_explanation": "You bring tenderness; Aquarius brings perspective. Together, you may learn to love without control.",
        "intimacy_explanation": "This is intimacy in unexpected ways—less about passion, more about connection that feels beautifully unique."
    },
    "Pisces": {
        "overall": 90,
        "communication": 85,
        "emotional": 95,
        "intimacy": 95,
        "overall_explanation": "With another Pisces, your connection is emotional, intuitive, and deeply soulful. You understand each other in ways words can't explain.",
        "communication_explanation": "You speak the language of dreams, feelings, and subtle energies. No need to over-explain—it just flows.",
        "emotional_explanation": "You hold each other with empathy and gentleness. The emotional safety here is rare and healing.",
        "intimacy_explanation": "Deep, ethereal, and spiritually charged. It's not just physical—it's almost cosmic."
    }
}
}

def calculate_compatibility(sign1, sign2):
    if sign1 in compatibility_data and sign2 in compatibility_data[sign1]:
        data = compatibility_data[sign1][sign2]
        return {
            "sign1": sign1,
            "sign2": sign2,
            "overall_score": data["overall"],
            "communication_score": data["communication"],
            "emotional_score": data["emotional"],
            "intimacy_score": data["intimacy"],
            "overall_explanation": data["overall_explanation"],
            "communication_explanation": data["communication_explanation"],
            "emotional_explanation": data["emotional_explanation"],
            "intimacy_explanation": data["intimacy_explanation"]
        }
    else:
        return {
            "error": "Compatibility data not found for the given signs.",
            "sign1": sign1,
            "sign2": sign2
        }


# Example usage
#print(json.dumps(calculate_compatibility("Aries", "Taurus")))
