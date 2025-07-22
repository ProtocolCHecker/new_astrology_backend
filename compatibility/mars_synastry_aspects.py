class MarsSynastryAspects:
    def __init__(self):
        self.aspects = {
            "Mars Conjunction Sun": "You'll experience intense mutual attraction and dynamic energy with your partner. They activate and energize your confidence, while you inspire their drive and ambition. This creates strong physical chemistry, but be mindful of power struggles.",
            "Mars Opposition Sun": "Your relationship has a magnetic 'opposites attract' dynamic with significant tension. Your partner challenges your identity, which can lead to exciting romantic tension or ongoing power struggles. Balance assertiveness with cooperation for a passionate, dynamic relationship.",
            "Mars Trine Sun": "You naturally support and encourage each other's goals and self-expression. There's easy physical chemistry and mutual respect, creating a supportive and action-oriented partnership where both of you feel energized and confident together.",
            "Mars Sextile Sun": "Your partner helps motivate you toward your goals, while you give direction to their energy. This creates friendly, supportive dynamics with moderate physical attraction and good cooperation, inspiring each other's best qualities.",
            "Mars Square Sun": "You may face significant tension and challenges with your partner, as their actions and desires clash with your ego. Strong initial attraction can lead to ongoing friction, but working through these challenges can create growth and passionate engagement.",
            "Mars Conjunction Moon": "You share an intense emotional and physical connection with your partner. They ignite your feelings and instincts, while you nurture their desires. This creates strong sexual chemistry but can also lead to volatility if not handled with care.",
            "Mars Opposition Moon": "Your relationship has emotional tension with magnetic attraction. You may find your partner too moody, while they see you as too harsh. This creates push-pull dynamics but also passionate intensity.",
            "Mars Trine Moon": "You naturally understand each other's emotional needs and support each other's ambitions. This creates warm, nurturing, and passionate relationships where both of you feel valued and encouraged.",
            "Mars Sextile Moon": "Your partner helps you express your feelings more directly, while you soften their approach. This creates supportive and caring dynamics, fostering a gentle emotional stimulation between you.",
            "Mars Square Moon": "You may experience emotional friction and timing issues with your partner. Their actions often upset your emotional security, while your moods frustrate their directness. Patience and understanding are key to making this work.",
            "Mars Conjunction Ascendant": "You feel an instant physical attraction and immediate impact with your partner. They find you very attractive and want to pursue you actively, creating dynamic and action-oriented partnerships.",
            "Mars Opposition Ascendant": "Your relationship has strong attraction with power struggles. Your partner challenges your self-presentation, while you may find them too aggressive. This creates exciting but potentially conflictual dynamics.",
            "Mars Trine Ascendant": "You share a natural attraction and easy rapport with your partner. They encourage your self-expression, while you inspire their confidence, creating harmonious and supportive connections.",
            "Mars Sextile Ascendant": "Your partner helps you be more assertive, while you appreciate their directness. This creates friendly and stimulating interactions, fostering gentle attraction and mutual encouragement.",
            "Mars Square Ascendant": "You may feel attraction with friction as your partner's approach clashes with your style. This creates tension about methods and presentation but can be stimulating with compromise.",
            "Mars Conjunction Mercury": "Your mental and physical energy combine with your partner's, stimulating your thinking and communication. They help you articulate your goals, creating dynamic conversations and shared activities.",
            "Mars Opposition Mercury": "You engage in mental sparring and debate with your partner. They find you too theoretical, while you think they are too impulsive. This creates stimulating but argumentative exchanges.",
            "Mars Trine Mercury": "You share harmonious mental and physical coordination with your partner. They inspire your ideas, while you help them plan effectively, creating productive and intellectually stimulating partnerships.",
            "Mars Sextile Mercury": "Your partner encourages your communication, while you help them think things through. This creates supportive intellectual exchange and gentle mental stimulation.",
            "Mars Square Mercury": "You may experience mental friction and impatience with your partner. They find you too slow, while you see them as too hasty. This creates challenging but potentially growth-oriented debates.",
            "Mars Conjunction Venus": "You share intense romantic and sexual attraction with your partner. They are drawn to your beauty and charm, while you are excited by their passion, creating powerful romantic chemistry.",
            "Mars Opposition Venus": "Your relationship has magnetic sexual tension. Your partner finds you irresistible but may be too aggressive, while you want more romance. This creates passionate but potentially volatile dynamics.",
            "Mars Trine Venus": "You naturally appeal to each other's romantic ideals, creating harmonious and balanced relationships. Your partner softens your approach, while you add passion to their romance, fostering loving connections.",
            "Mars Sextile Venus": "Your partner helps you express affection more directly, while you add grace to their approach. This creates pleasant and harmonious connections with gentle romantic attraction.",
            "Mars Square Venus": "You may experience romantic tension and different styles with your partner. Your directness clashes with their need for romance, creating friction about intimacy styles that requires understanding and compromise.",
            "Mars Conjunction Mars": "You share drive and similar energy levels with your partner. Both of you have comparable ambition and approach to action, creating great teamwork or competition. Be mindful of both wanting to lead.",
            "Mars Opposition Mars": "You have competing drives and conflicting methods with your partner. Both of you are assertive but in different ways, creating power struggles that require learning to take turns leading.",
            "Mars Trine Mars": "You share harmonious action and mutual support with your partner. Both of you understand each other's ambitions and work well together, creating dynamic and supportive partnerships with shared goals.",
            "Mars Sextile Mars": "You complement each other's energy and encourage each other's ambitions without major conflict. This creates motivating and supportive dynamics with gentle competition.",
            "Mars Square Mars": "You have clashing drives and competing agendas with your partner. Both of you are assertive but in conflicting ways, creating ongoing tension about methods and timing that requires patience and compromise.",
            "Mars Conjunction Jupiter": "You feel expanded energy and shared adventures with your partner. They inspire and give you confidence, while you enjoy their enthusiasm, creating optimistic and adventurous partnerships.",
            "Mars Opposition Jupiter": "You may find your partner too philosophical or excessive, while they see you as too narrow-focused. This creates tension about scope and approach, requiring balance and understanding.",
            "Mars Trine Jupiter": "You inspire each other's optimism and expand each other's horizons. This creates growth-oriented and positive relationships with harmonious expansion and mutual encouragement.",
            "Mars Sextile Jupiter": "Your partner helps you take action on ideas, while you broaden their perspective. This creates supportive and encouraging dynamics with gentle expansion and opportunity.",
            "Mars Square Jupiter": "You may find your partner too excessive or theoretical, while they see you as too impatient. This creates tension about timing and scope, requiring compromise and understanding.",
            "Mars Conjunction Saturn": "You feel disciplined energy and serious commitment with your partner. They ground you with stability, while you appreciate their drive, creating practical and long-term focused partnerships.",
            "Mars Opposition Saturn": "You feel limited by your partner's caution, while they find you too reckless. This creates tension about timing and responsibility, requiring balance and patience.",
            "Mars Trine Saturn": "You benefit from each other's discipline and directed energy. Your partner provides structure, while you energize their drive, creating productive and stable relationships with harmonious structure.",
            "Mars Sextile Saturn": "Your partner helps you be more decisive, while you help them be more strategic. This creates supportive and building dynamics with gentle structure and practical action.",
            "Mars Square Saturn": "You feel blocked by your partner's restrictions, while they find you too impulsive. This creates challenging but potentially maturing dynamics that require understanding and compromise.",
            "Mars Conjunction Uranus": "You share electric attraction and unpredictable energy with your partner. They excite you with their uniqueness, while you appreciate their directness, creating dynamic but potentially unstable connections.",
            "Mars Opposition Uranus": "You find your partner too erratic, while they see you as too conventional. This creates exciting but unstable dynamics that require flexibility and mutual respect for differing outlooks.",
            "Mars Trine Uranus": "You encourage each other's uniqueness and independence, creating exciting and liberating relationships with harmonious innovation and freedom.",
            "Mars Sextile Uranus": "Your partner helps you take action on ideas, while you add excitement to their life. This creates stimulating and friendly dynamics with gentle innovation and friendship.",
            "Mars Square Uranus": "Your methods clash with your partner's need for freedom, creating unpredictable conflicts. Flexibility and independence are key to making this work.",
            "Mars Conjunction Neptune": "You share passionate idealism and spiritual connection with your partner. They inspire you with their vision, while you energize their passion, creating romantic and idealistic but potentially confusing bonds.",
            "Mars Opposition Neptune": "You find your partner too vague or deceptive, while they see you as too harsh. This creates confusion about intentions, requiring clear communication and understanding.",
            "Mars Trine Neptune": "You help each other manifest dreams, adding spiritual dimension to your actions. This creates inspiring and compassionate relationships with harmonious inspiration and compassion.",
            "Mars Sextile Neptune": "Your partner encourages your artistic expression, while you add sensitivity to their approach. This creates supportive and creative dynamics with gentle inspiration and creativity.",
            "Mars Square Neptune": "Your directness clashes with your partner's subtlety, creating misunderstandings about intentions and methods. Clear communication and patience are essential for harmony.",
            "Mars Conjunction Pluto": "You share intense transformation and power with your partner. They are drawn to your intensity, while you energize their passion, creating powerful and transformative but potentially obsessive connections.",
            "Mars Opposition Pluto": "You feel challenged by your partner's depth, while they find you too surface-level. This creates magnetic but potentially destructive dynamics that require conscious transformation and understanding.",
            "Mars Trine Pluto": "You help each other express power constructively, adding depth to your passion. This creates empowering and transformative relationships with harmonious transformation and empowerment.",
            "Mars Sextile Pluto": "Your partner encourages your regeneration, while you add depth to their actions. This creates supportive and empowering dynamics with gentle transformation and mutual empowerment.",
            "Mars Square Pluto": "Your directness clashes with your partner's intensity, creating potentially destructive conflicts about control and power. Conscious transformation and mutual respect are key to making this work.",
            "Mars Conjunction Medium Coeli": "Your drive and energy align perfectly with your partner's career ambitions. You provide powerful motivation that propels them toward professional success, often becoming the driving force behind their career advancement.",
            "Mars Opposition Medium Coeli": "Your aggressive energy may conflict with your partner's career requirements. You might feel that your drive doesn't align with their professional needs, creating tension between personal drive and professional requirements.",
            "Mars Trine Medium Coeli": "Your energy and drive naturally support your partner's professional goals. You provide excellent motivation that enhances their career success, creating harmonious channeling of personal drive into professional achievement.",
            "Mars Sextile Medium Coeli": "You have the opportunity to contribute energy and drive to your partner's career development. Your motivation can be directed to support their professional advancement, offering excellent potential for dynamic collaboration.",
            "Mars Square Medium Coeli": "Your drive may clash with your partner's professional requirements. You might feel that your energy undermines their career goals, creating friction between personal assertiveness and professional effectiveness."
        }

    def get_aspect_interpretation(self, aspect_name):
        return self.aspects.get(aspect_name, "Aspect interpretation not found.")

    def add_aspect(self, aspect_name, interpretation):
        self.aspects[aspect_name] = interpretation

    def remove_aspect(self, aspect_name):
        if aspect_name in self.aspects:
            del self.aspects[aspect_name]
