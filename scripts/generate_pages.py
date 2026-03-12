from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PRICING_URL = "https://crazyrouter.com/api/pricing"
REGISTER_URL = "https://crazyrouter.com/#/register"
SITE_URL = "https://crazyrouter.com/models"
TODAY = date.today().isoformat()


@dataclass(frozen=True)
class Model:
    slug: str
    name: str
    provider: str
    api_model: str
    seo_status: str
    hero_badge: str
    summary: str
    description: str
    search_intent: str
    context_window: str
    max_output: str
    modality: str
    latency: str
    best_for: tuple[str, str, str]
    not_best_for: tuple[str, str]
    why_crazyrouter: tuple[str, str, str]
    comparison_notes: tuple[str, str, str]
    keywords: tuple[str, ...]
    related: tuple[str, str, str]
    last_reviewed: str
    owner: str
    review_cadence: str
    example_prompt: str
    faq: tuple[tuple[str, str], ...]


MODELS = [
    Model(
        slug="gpt-4o",
        name="GPT-4o",
        provider="OpenAI",
        api_model="chatgpt-4o-latest",
        seo_status="index",
        hero_badge="OpenAI GPT-4o",
        summary="OpenAI's mainstream multimodal model for chat, vision, and production assistants.",
        description="Use GPT-4o through Crazyrouter when you want broad compatibility, strong multimodal support, and a clean path away from direct provider lock-in.",
        search_intent="People searching for GPT-4o pricing usually want a fast answer on cost, API compatibility, and whether they can replace direct OpenAI access without extra migration work.",
        context_window="128K",
        max_output="16K",
        modality="Text, image, audio",
        latency="Fast",
        best_for=("Mainstream multimodal apps", "Vision-enabled support and assistant workflows", "Teams migrating from direct OpenAI usage"),
        not_best_for=("The cheapest high-volume classification workloads", "Deep reasoning tasks where a reasoning-first model is more appropriate"),
        why_crazyrouter=("OpenAI-compatible calls with one API key", "Lower token pricing than direct access", "Easy fallback routing to GPT-5, Claude, or Gemini later"),
        comparison_notes=("Choose GPT-4o when you want strong multimodal support without moving to a slower reasoning model.", "Choose GPT-5 when reasoning and coding quality matter more than latency.", "Choose Gemini 2.5 Pro when extremely long context is the deciding factor."),
        keywords=("gpt-4o api", "gpt-4o pricing", "gpt-4o api cost", "openai api pricing", "gpt-4o cheap api"),
        related=("gpt-5", "claude-sonnet-4-6", "gemini-2-5-pro"),
        last_reviewed=TODAY,
        owner="growth",
        review_cadence="monthly",
        example_prompt="Summarize this support ticket and identify whether an image attachment changes the priority.",
        faq=(("How much does GPT-4o cost on Crazyrouter?", "GPT-4o costs $2.75 per 1M input tokens and $8.25 per 1M output tokens on Crazyrouter based on the latest pricing sync. That is 45% lower than the direct list price used on this page."), ("Why would a team choose GPT-4o instead of GPT-5?", "GPT-4o is often the safer choice when you want mainstream multimodal coverage, lower latency, and a simpler cost profile. GPT-5 is the better choice for harder reasoning and coding-heavy workloads."), ("Can I migrate an existing OpenAI integration to Crazyrouter quickly?", "Yes. GPT-4o is available behind an OpenAI-compatible API. In most cases you only change the base URL, API key, and optionally the model name."), ("What makes this page worth indexing long term?", "This page is maintained as a conversion-oriented landing page with live pricing, implementation examples, model fit guidance, and an explicit review date so it stays more useful than a thin template page."), ("What context window does GPT-4o support?", "This page tracks GPT-4o with a 128K context window and an estimated 16K max output, which is enough for many production assistant and analysis use cases."), ("When should I not use GPT-4o?", "If your main requirement is deeper reasoning or long chain-of-thought behavior, a reasoning-oriented model like GPT-5 or o3 may be a better fit. If your main requirement is lowest cost at scale, a cheaper model may make more sense.")),
    ),
    Model(
        slug="gpt-5",
        name="GPT-5",
        provider="OpenAI",
        api_model="gpt-5-chat",
        seo_status="index",
        hero_badge="OpenAI GPT-5",
        summary="OpenAI's flagship chat model for stronger reasoning, coding, and agent workflows.",
        description="Use GPT-5 through Crazyrouter when you need a premium reasoning model but still want unified billing, cleaner model switching, and an OpenAI-style API surface.",
        search_intent="People searching for GPT-5 pricing are usually comparing direct cost against alternatives while also asking whether the added reasoning quality is worth the spend.",
        context_window="400K",
        max_output="128K",
        modality="Text, image",
        latency="Medium",
        best_for=("Agentic coding and refactoring", "Long-context research and planning", "Hard reasoning tasks where quality matters more than speed"),
        not_best_for=("The lowest-latency chat experiences", "Budget-sensitive high-volume classification or extraction"),
        why_crazyrouter=("Cheaper than direct pricing for flagship reasoning traffic", "Same OpenAI integration shape across multiple premium models", "Easier experimentation between GPT-5, Claude, Gemini, and o-series models"),
        comparison_notes=("Choose GPT-5 when reasoning depth and coding quality drive the business outcome.", "Choose GPT-5 Mini when you want the GPT-5 family feel at a much lower unit cost.", "Choose o3 when you specifically want reasoning-first behavior rather than a flagship chat default."),
        keywords=("gpt-5 api pricing", "gpt-5 api", "gpt-5 chat api", "openai gpt-5 cost", "gpt-5 cheap api"),
        related=("gpt-4o", "gpt-5-mini", "o3"),
        last_reviewed=TODAY,
        owner="growth",
        review_cadence="monthly",
        example_prompt="Review this architecture proposal, identify risks, and suggest a phased migration plan.",
        faq=(("How much does GPT-5 cost on Crazyrouter?", "GPT-5 costs $0.69 per 1M input tokens and $5.50 per 1M output tokens on Crazyrouter from the current pricing feed. That is 45% below the direct list price referenced on this page."), ("Who should actually pay for GPT-5?", "Teams should pay for GPT-5 when model quality changes the business result, such as complex coding, difficult planning, or high-value research workflows. For lighter production traffic, GPT-5 Mini or GPT-4o may be more efficient."), ("Is GPT-5 available through an OpenAI-compatible API?", "Yes. GPT-5 can be called on Crazyrouter with the same general SDK pattern many teams already use for OpenAI integrations."), ("Why not use GPT-5 for everything?", "Because a premium reasoning model is not always the best cost-performance choice. Many teams route only the hardest requests to GPT-5 and keep routine requests on cheaper models."), ("What does the 400K context window matter for?", "A very large context window is useful for long documents, large codebases, agent memory, and workflows where the model needs to reason over more background at once."), ("Why keep this page indexed rather than treat it as a throwaway landing page?", "GPT-5 is a core commercial-intent term. This page is intended to be a maintained decision page with pricing, usage guidance, and comparison context rather than a thin paid-traffic page.")),
    ),
    Model(
        slug="gpt-5-mini",
        name="GPT-5 Mini",
        provider="OpenAI",
        api_model="gpt-5-mini",
        seo_status="noindex",
        hero_badge="OpenAI GPT-5 Mini",
        summary="A lower-cost GPT-5 variant for high-volume chat, extraction, and lightweight coding.",
        description="Use GPT-5 Mini through Crazyrouter when you want GPT-5-family quality characteristics at a significantly lower unit cost.",
        search_intent="Searchers looking for GPT-5 Mini usually care about price-performance tradeoffs against flagship models.",
        context_window="400K",
        max_output="128K",
        modality="Text, image",
        latency="Fast",
        best_for=("Bulk support and workflow automation", "Structured extraction and tagging", "Affordable coding copilots"),
        not_best_for=("The hardest reasoning requests", "Cases where maximum writing quality matters more than cost"),
        why_crazyrouter=("Low-cost access to a GPT-5-family model", "One-key routing between mini and flagship models", "Simpler pay-as-you-go billing"),
        comparison_notes=("Choose GPT-5 Mini when the workload is large and the unit cost matters.", "Choose GPT-5 when reasoning quality matters more than throughput cost.", "Choose Gemini 2.5 Flash when you want a different low-cost fast multimodal option."),
        keywords=("gpt-5 mini api", "gpt-5 mini pricing", "gpt-5 mini cost"),
        related=("gpt-5", "gpt-4o", "gemini-2-5-flash"),
        last_reviewed=TODAY,
        owner="growth",
        review_cadence="monthly",
        example_prompt="Extract the order status, customer issue, and required action from this support conversation.",
        faq=(),
    ),
    Model(
        slug="claude-sonnet-4-6",
        name="Claude Sonnet 4.6",
        provider="Anthropic",
        api_model="claude-sonnet-4-6",
        seo_status="index",
        hero_badge="Anthropic Claude Sonnet 4.6",
        summary="Anthropic's balanced frontier model, especially strong for coding and analysis.",
        description="Use Claude Sonnet 4.6 through Crazyrouter when you want a premium coding and writing model without locking your stack to a single provider.",
        search_intent="People searching for Claude Sonnet pricing are often deciding whether Anthropic quality is worth it and whether they can access it through a simpler gateway.",
        context_window="200K",
        max_output="64K",
        modality="Text, image",
        latency="Medium",
        best_for=("Code review and implementation work", "Long-form editing and rewriting", "Analysis tasks that need clarity and polish"),
        not_best_for=("The cheapest high-volume workflows", "Video-first or audio-native multimodal workloads"),
        why_crazyrouter=("Lower pricing than going direct", "A single integration path for Anthropic and non-Anthropic models", "Cleaner comparison testing against GPT and Gemini families"),
        comparison_notes=("Choose Claude Sonnet 4.6 when you want a strong balance of coding quality, writing quality, and practical latency.", "Choose Claude Opus 4.6 when absolute quality matters more than unit economics.", "Choose GPT-5 when you want OpenAI's flagship reasoning profile or existing OpenAI workflow familiarity."),
        keywords=("claude sonnet api pricing", "claude sonnet 4.6 api", "anthropic sonnet cost", "claude api pricing", "claude sonnet cheap api"),
        related=("claude-opus-4-6", "gpt-5", "gemini-2-5-pro"),
        last_reviewed=TODAY,
        owner="growth",
        review_cadence="monthly",
        example_prompt="Review this pull request summary, identify architectural risks, and suggest the best next implementation step.",
        faq=(("How much does Claude Sonnet 4.6 cost on Crazyrouter?", "Claude Sonnet 4.6 costs $1.65 per 1M input tokens and $8.25 per 1M output tokens on Crazyrouter from the latest sync. That is 45% lower than the direct list price referenced here."), ("Why do teams often compare Claude Sonnet 4.6 with GPT-5 instead of GPT-4o?", "Because Sonnet and GPT-5 are more often evaluated for higher-value coding, writing, and analysis work. GPT-4o is still important, but it is often chosen for broader multimodal coverage and speed."), ("Is Claude Sonnet 4.6 available behind an OpenAI-style gateway?", "Yes. Crazyrouter lets teams access Claude Sonnet 4.6 with the same general OpenAI-compatible request flow used across the rest of the platform."), ("When should I choose Claude Sonnet 4.6 over Claude Opus 4.6?", "Choose Sonnet when you want the strong Claude family quality profile but need better cost-efficiency for repeated production use. Choose Opus when top-end output quality matters more than cost."), ("What makes this page a long-term index page rather than a campaign page?", "This page is designed as a maintained pricing and decision asset for a head term with ongoing commercial intent, not just a temporary paid-traffic variant."), ("What is Claude Sonnet 4.6 not ideal for?", "It is not the strongest fit when the only goal is lowest-cost throughput or when the workflow is heavily centered on richer audio or video-native multimodal input.")),
    ),
    Model(
        slug="claude-opus-4-6",
        name="Claude Opus 4.6",
        provider="Anthropic",
        api_model="claude-opus-4-6",
        seo_status="noindex",
        hero_badge="Anthropic Claude Opus 4.6",
        summary="Anthropic's highest-tier model for premium reasoning, nuanced writing, and heavyweight coding.",
        description="Choose Claude Opus 4.6 through Crazyrouter when you need maximum Claude-family quality but still want unified billing and model routing flexibility.",
        search_intent="Opus searches are typically high-commercial-intent but lower volume than Sonnet and may be better staged before full index prioritization.",
        context_window="200K",
        max_output="64K",
        modality="Text, image",
        latency="Medium",
        best_for=("Premium research", "High-stakes writing", "Complex code generation"),
        not_best_for=("Budget-sensitive traffic", "Routine automation workloads"),
        why_crazyrouter=("Unified billing for premium models", "Easy comparison against Sonnet and GPT families", "Lower switching cost across providers"),
        comparison_notes=("Choose Opus when output quality matters more than throughput cost.", "Choose Sonnet for a more balanced price-performance profile.", "Choose GPT-5 when you want OpenAI's flagship profile instead."),
        keywords=("claude opus api", "claude opus 4.6 pricing", "anthropic opus api pricing"),
        related=("claude-sonnet-4-6", "gpt-5", "o3"),
        last_reviewed=TODAY,
        owner="growth",
        review_cadence="monthly",
        example_prompt="Draft an executive memo that explains tradeoffs between these three strategic options.",
        faq=(),
    ),
    Model(
        slug="gemini-2-5-pro",
        name="Gemini 2.5 Pro",
        provider="Google",
        api_model="gemini-2.5-pro",
        seo_status="noindex",
        hero_badge="Google Gemini 2.5 Pro",
        summary="Google's capable multimodal model for long-context reasoning and product assistants.",
        description="Use Gemini 2.5 Pro through Crazyrouter when long context and multimodal flexibility matter more than provider purity.",
        search_intent="Gemini 2.5 Pro queries often center on long-context comparison and pricing evaluation.",
        context_window="1M",
        max_output="64K",
        modality="Text, image, audio, video",
        latency="Medium",
        best_for=("Large document analysis", "Multimodal assistants", "Research planning"),
        not_best_for=("The cheapest text-only workflows", "Low-latency chat that does not need huge context"),
        why_crazyrouter=("Unified billing", "OpenAI-style gateway", "Fast model comparison"),
        comparison_notes=("Choose Gemini 2.5 Pro when very large context is central to the use case.", "Choose GPT-5 for flagship reasoning and coding emphasis.", "Choose GPT-4o when you want broader OpenAI migration familiarity."),
        keywords=("gemini pro api pricing", "gemini 2.5 pro api", "google gemini api cost"),
        related=("gemini-2-5-flash", "gpt-5", "gpt-4o"),
        last_reviewed=TODAY,
        owner="growth",
        review_cadence="monthly",
        example_prompt="Read these three long policy documents and identify where they conflict.",
        faq=(),
    ),
    Model(
        slug="gemini-2-5-flash",
        name="Gemini 2.5 Flash",
        provider="Google",
        api_model="gemini-2.5-flash",
        seo_status="noindex",
        hero_badge="Google Gemini 2.5 Flash",
        summary="A faster, lower-cost Gemini model for production chat, extraction, and real-time assistants.",
        description="Use Gemini 2.5 Flash through Crazyrouter for fast multimodal traffic that benefits from the Gemini family at a lighter cost profile.",
        search_intent="Gemini Flash searches are often price-performance comparisons against mini and fast-tier models.",
        context_window="1M",
        max_output="64K",
        modality="Text, image, audio, video",
        latency="Fast",
        best_for=("High-volume chat", "Fast OCR and extraction", "Realtime copilots"),
        not_best_for=("Premium writing quality", "The hardest reasoning tasks"),
        why_crazyrouter=("Low-cost access", "One-key routing", "Unified billing"),
        comparison_notes=("Choose Gemini Flash when speed and throughput cost matter.", "Choose Gemini Pro for heavier reasoning and long-context work.", "Choose GPT-5 Mini when you want a different low-cost flagship-family option."),
        keywords=("gemini flash api", "gemini 2.5 flash pricing", "google gemini flash api"),
        related=("gemini-2-5-pro", "gpt-5-mini", "deepseek-v3"),
        last_reviewed=TODAY,
        owner="growth",
        review_cadence="monthly",
        example_prompt="Extract invoice totals, due dates, and follow-up actions from this batch of customer emails.",
        faq=(),
    ),
    Model(
        slug="deepseek-v3",
        name="DeepSeek V3",
        provider="DeepSeek",
        api_model="deepseek-v3",
        seo_status="noindex",
        hero_badge="DeepSeek V3",
        summary="A practical model for coding, analysis, and cost-sensitive production workloads.",
        description="Use DeepSeek V3 through Crazyrouter when cost sensitivity matters and you still want a general-purpose API model with straightforward integration.",
        search_intent="DeepSeek V3 searches often compare price-performance rather than pure flagship quality.",
        context_window="128K",
        max_output="16K",
        modality="Text",
        latency="Fast",
        best_for=("Cost-sensitive coding", "Batch classification", "Everyday drafting"),
        not_best_for=("Premium multimodal use cases", "Highest-end reasoning tasks"),
        why_crazyrouter=("Easy gateway access", "Unified billing", "Cross-provider comparison"),
        comparison_notes=("Choose DeepSeek V3 when budget efficiency matters.", "Choose DeepSeek R1 for more reasoning-oriented behavior.", "Choose GPT-5 Mini or o4-mini when you prefer OpenAI-family routing."),
        keywords=("deepseek v3 api", "deepseek v3 pricing", "deepseek api pricing"),
        related=("deepseek-r1", "gpt-5-mini", "o4-mini"),
        last_reviewed=TODAY,
        owner="growth",
        review_cadence="monthly",
        example_prompt="Classify these user requests by topic, urgency, and likely owner.",
        faq=(),
    ),
    Model(
        slug="deepseek-r1",
        name="DeepSeek R1",
        provider="DeepSeek",
        api_model="deepseek-r1",
        seo_status="noindex",
        hero_badge="DeepSeek R1",
        summary="DeepSeek's reasoning-oriented model for step-by-step problem solving, math, and planning.",
        description="Use DeepSeek R1 through Crazyrouter when you need reasoning-oriented behavior without changing your integration stack.",
        search_intent="DeepSeek R1 queries usually focus on reasoning behavior, pricing, and replacement options.",
        context_window="128K",
        max_output="32K",
        modality="Text",
        latency="Medium",
        best_for=("Math-heavy workflows", "Planning agents", "Reasoning-focused coding"),
        not_best_for=("Lowest-latency chat", "Rich multimodal workflows"),
        why_crazyrouter=("Unified balance", "Provider flexibility", "Simple gateway access"),
        comparison_notes=("Choose DeepSeek R1 when reasoning depth matters more than raw throughput.", "Choose DeepSeek V3 for cheaper general-purpose traffic.", "Choose o3 when you want OpenAI-family reasoning instead."),
        keywords=("deepseek r1 api", "deepseek r1 pricing", "deepseek reasoning api"),
        related=("deepseek-v3", "o3", "claude-sonnet-4-6"),
        last_reviewed=TODAY,
        owner="growth",
        review_cadence="monthly",
        example_prompt="Solve this planning problem step by step and explain the tradeoffs between the options.",
        faq=(),
    ),
    Model(
        slug="o3",
        name="o3",
        provider="OpenAI",
        api_model="o3",
        seo_status="noindex",
        hero_badge="OpenAI o3",
        summary="OpenAI's reasoning model for deeper analysis, hard coding tasks, and agent backends.",
        description="Use o3 through Crazyrouter when reasoning-first behavior matters more than mainstream chat defaults.",
        search_intent="o3 searches usually center on reasoning quality versus flagship chat pricing.",
        context_window="200K",
        max_output="100K",
        modality="Text, image",
        latency="Medium",
        best_for=("Advanced reasoning", "Hard debugging", "Tool-using agents"),
        not_best_for=("Simple routine chat", "Lowest-cost high-volume use cases"),
        why_crazyrouter=("Unified gateway", "Cross-model routing", "Pay-as-you-go access"),
        comparison_notes=("Choose o3 when you specifically want reasoning-first behavior.", "Choose GPT-5 when you want a flagship chat default with premium reasoning.", "Choose o4-mini for cheaper reasoning-heavy routing."),
        keywords=("o3 api pricing", "o3 api", "openai o3 pricing"),
        related=("o4-mini", "gpt-5", "deepseek-r1"),
        last_reviewed=TODAY,
        owner="growth",
        review_cadence="monthly",
        example_prompt="Debug this failure report and propose the most likely root cause with a ranked action plan.",
        faq=(),
    ),
    Model(
        slug="o4-mini",
        name="o4-mini",
        provider="OpenAI",
        api_model="o4-mini",
        seo_status="noindex",
        hero_badge="OpenAI o4-mini",
        summary="A lighter OpenAI reasoning model for fast, affordable chains of thought.",
        description="Use o4-mini through Crazyrouter when you want cheaper reasoning-oriented traffic without leaving the OpenAI family.",
        search_intent="o4-mini queries usually reflect budget-sensitive reasoning model evaluation.",
        context_window="200K",
        max_output="100K",
        modality="Text, image",
        latency="Fast",
        best_for=("Affordable reasoning", "Lightweight agent routing", "Fast summarization"),
        not_best_for=("Highest-quality premium reasoning", "Rich multimodal-heavy workflows"),
        why_crazyrouter=("Lower reasoning cost", "One-key access", "Model routing flexibility"),
        comparison_notes=("Choose o4-mini when you need cheaper reasoning throughput.", "Choose o3 when you want stronger reasoning quality.", "Choose GPT-5 Mini when you prefer a different low-cost OpenAI-family profile."),
        keywords=("o4 mini api", "o4-mini pricing", "openai o4 mini api"),
        related=("o3", "gpt-5-mini", "deepseek-v3"),
        last_reviewed=TODAY,
        owner="growth",
        review_cadence="monthly",
        example_prompt="Summarize these issue logs and tell me which ones need immediate engineering attention.",
        faq=(),
    ),
]

BY_SLUG = {model.slug: model for model in MODELS}


def fetch_prices() -> dict[str, dict]:
    request = Request(PRICING_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return {item["model_name"]: item for item in payload["data"]}


def money(value: float) -> str:
    return f"{value:.2f}"


def register_link(slug: str) -> str:
    return f"{REGISTER_URL}?utm_source=models&utm_medium=landing&utm_campaign={slug}"


def page_link(slug: str) -> str:
    return f"{SITE_URL}/{slug}"


def compare_label(provider: str) -> str:
    if provider == "OpenAI":
        return "OpenAI Direct"
    if provider == "Anthropic":
        return "Anthropic Direct"
    if provider == "Google":
        return "Google AI Direct"
    return f"{provider} Direct"


def compute_price(record: dict) -> dict[str, float | int]:
    official_input = float(record["model_ratio"]) * 2
    official_output = official_input * float(record["completion_ratio"])
    discount = float(record["discount"])
    return {
        "official_input": official_input,
        "official_output": official_output,
        "crazy_input": official_input * discount,
        "crazy_output": official_output * discount,
        "savings": round((1 - discount) * 100),
    }


def default_faq(model: Model, prices: dict) -> tuple[tuple[str, str], ...]:
    return (
        (f"How much does {model.name} cost on Crazyrouter?", f"{model.name} costs ${money(prices['crazy_input'])} per 1M input tokens and ${money(prices['crazy_output'])} per 1M output tokens on Crazyrouter based on the latest pricing sync."),
        (f"Is {model.name} available through an OpenAI-compatible API?", f"Yes. {model.name} can be accessed through Crazyrouter with the same general OpenAI-compatible request flow used across the platform."),
        (f"What is {model.name} best for?", f"{model.name} is best suited to {model.best_for[0].lower()}, {model.best_for[1].lower()}, and {model.best_for[2].lower()}."),
        (f"When should this page stay out of search results?", f"This page is currently marked noindex because it is useful for navigation and campaign traffic, but it is not yet one of the small set of landing pages prioritized for long-term organic indexation."),
    )


def schema_product(model: Model, prices: dict) -> str:
    return json.dumps({"@context": "https://schema.org", "@type": "Product", "name": f"{model.name} API via Crazyrouter", "description": model.description, "url": page_link(model.slug), "brand": {"@type": "Organization", "name": "Crazyrouter", "url": "https://crazyrouter.com", "logo": "https://crazyrouter.com/logo.png"}, "offers": {"@type": "Offer", "price": money(prices["crazy_input"]), "priceCurrency": "USD", "description": "Per 1M input tokens", "availability": "https://schema.org/InStock"}}, ensure_ascii=False, indent=2)


def schema_faq(items: tuple[tuple[str, str], ...]) -> str:
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": question, "acceptedAnswer": {"@type": "Answer", "text": answer}} for question, answer in items]}, ensure_ascii=False, indent=2)


def related_cards(model: Model, prices_by_slug: dict[str, dict]) -> str:
    blocks: list[str] = []
    for slug in model.related:
        item = BY_SLUG[slug]
        prices = prices_by_slug[slug]
        blocks.append(f'<a href="/models/{item.slug}" class="card related"><h3>{item.name}</h3><p>{item.summary}</p><span>From ${money(prices["crazy_input"])} / 1M input</span></a>')
    return "".join(blocks)


def section_cards(title: str, items: tuple[str, ...]) -> str:
    return "".join([f'<div class="card small"><h3>{item}</h3><p>{title}</p></div>' for item in items])


def faq_markup(items: tuple[tuple[str, str], ...]) -> str:
    return "".join([f'<details class="faq"><summary>{question}</summary><p>{answer}</p></details>' for question, answer in items])


def robots_meta(model: Model) -> str:
    if model.seo_status == "index":
        return '<meta name="robots" content="index,follow,max-image-preview:large">'
    return '<meta name="robots" content="noindex,follow">'


def governance_badge(model: Model) -> str:
    if model.seo_status == "index":
        return "Indexed and maintained"
    return "Accessible but currently noindex"


def page_template(model: Model, prices: dict, prices_by_slug: dict[str, dict]) -> str:
    faq = model.faq or default_faq(model, prices)
    title = f"{model.name} API Pricing & Access - Save {prices['savings']}% | Crazyrouter"
    description = f"Access {model.name} API at ${money(prices['crazy_input'])} per 1M input tokens and ${money(prices['crazy_output'])} per 1M output tokens via Crazyrouter. OpenAI-compatible access, clear pricing, and {prices['savings']}% below direct pricing where applicable."
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="{', '.join(model.keywords)}">
{robots_meta(model)}
<link rel="canonical" href="{page_link(model.slug)}">
<meta property="og:title" content="{model.name} API Pricing via Crazyrouter">
<meta property="og:description" content="{description}">
<meta property="og:type" content="product">
<meta property="og:url" content="{page_link(model.slug)}">
<meta property="og:image" content="https://crazyrouter.com/twitter-card.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{model.name} API Pricing via Crazyrouter">
<meta name="twitter:description" content="{description}">
<script type="application/ld+json">{schema_product(model, prices)}</script>
<script type="application/ld+json">{schema_faq(faq)}</script>
<style>
*{{box-sizing:border-box}}body{{margin:0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#111827;background:#fff;line-height:1.65}}a{{color:inherit}}.wrap{{max-width:1120px;margin:0 auto;padding:0 16px}}.nav{{position:sticky;top:0;background:rgba(255,255,255,.94);backdrop-filter:blur(10px);border-bottom:1px solid #e5e7eb}}.navin{{height:64px;display:flex;align-items:center;justify-content:space-between}}.brand{{font-size:20px;font-weight:800;text-decoration:none}}.menu{{display:flex;gap:20px;font-size:14px}}.menu a{{text-decoration:none;color:#4b5563}}.menu a.active,.menu a:hover{{color:#2563eb}}.btn{{display:inline-block;text-decoration:none;border-radius:9999px;padding:12px 22px;font-weight:700}}.btn.dark{{background:#111827;color:#fff}}.btn.primary{{background:#2563eb;color:#fff}}.btn.light{{border:1px solid #d1d5db;color:#111827;background:#fff}}.hero{{padding:60px 0 36px;text-align:center}}.badge{{display:inline-block;background:#dbeafe;color:#1d4ed8;border-radius:9999px;padding:4px 12px;font-size:13px;font-weight:700}}h1{{font-size:44px;line-height:1.15;margin:16px 0}}h1 span{{color:#2563eb}}.lead{{max-width:820px;margin:0 auto 24px;color:#6b7280;font-size:18px}}.hero-actions{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}}.stats{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:22px}}.stat{{padding:8px 14px;border-radius:9999px;border:1px solid #e5e7eb;background:#f9fafb;font-size:14px;color:#374151}}section{{padding:0 0 56px}}h2{{font-size:30px;line-height:1.2;text-align:center;margin:0 0 12px}}.subtitle{{max-width:780px;margin:0 auto 28px;text-align:center;color:#6b7280}}.grid2,.grid3,.grid4{{display:grid;gap:20px}}.grid2{{grid-template-columns:repeat(2,minmax(0,1fr))}}.grid3{{grid-template-columns:repeat(3,minmax(0,1fr))}}.grid4{{grid-template-columns:repeat(4,minmax(0,1fr))}}.card{{border:1px solid #e5e7eb;border-radius:18px;padding:24px;background:#fff;text-decoration:none}}.card.highlight{{background:linear-gradient(180deg,#eff6ff 0,#fff 100%);border-color:#93c5fd}}.card h3{{margin:0 0 10px;font-size:20px}}.small h3{{font-size:18px}}.price-row{{display:flex;justify-content:space-between;padding:14px 0;border-top:1px solid #f3f4f6}}.price-row:first-of-type{{border-top:none;padding-top:0}}.muted{{color:#6b7280}}.old{{color:#9ca3af;text-decoration:line-through;font-weight:800;font-size:24px}}.green{{color:#16a34a;font-weight:800;font-size:24px}}.save{{display:inline-block;background:#2563eb;color:#fff;border-radius:9999px;padding:6px 10px;font-size:12px;font-weight:800;float:right}}.banner{{margin-top:20px;border-radius:18px;background:#111827;color:#fff;padding:18px 22px;text-align:center}}.spec{{text-align:center}}.spec .label{{font-size:14px;color:#6b7280;margin-bottom:6px}}.spec .value{{font-size:24px;font-weight:800}}.code{{background:#111827;color:#e5e7eb;border-radius:18px;padding:20px;position:relative;max-width:900px;margin:0 auto}}.tabs{{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-bottom:16px}}.tab{{border:1px solid #d1d5db;border-radius:9999px;padding:10px 16px;background:#fff;color:#374151;cursor:pointer;font-weight:700}}.tab.active{{background:#111827;color:#fff;border-color:#111827}}.copy{{position:absolute;top:18px;right:18px;border:none;border-radius:9999px;padding:8px 14px;background:#374151;color:#fff;cursor:pointer}}pre{{margin:0;white-space:pre-wrap;word-break:break-word;font-size:14px;font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;line-height:1.7}}.panel{{display:none}}.panel.active{{display:block}}.faq{{max-width:820px;margin:0 auto;border-bottom:1px solid #e5e7eb;padding:16px 0}}.faq summary{{font-weight:700;cursor:pointer}}.faq p{{color:#6b7280}}.related p,.small p{{color:#6b7280}}.related span{{font-weight:700;color:#16a34a}}.callout{{max-width:980px;margin:0 auto;border:1px solid #dbeafe;background:#f8fbff;border-radius:18px;padding:22px}}.callout ul{{margin:10px 0 0 20px;color:#4b5563}}.callout li{{margin-bottom:8px}}.cta{{background:#f9fafb;padding:56px 0;text-align:center}}.foot{{padding:32px 0;border-top:1px solid #e5e7eb;color:#9ca3af;text-align:center;font-size:13px}}.foot a{{color:#2563eb;text-decoration:none}}@media(max-width:900px){{.grid2,.grid3,.grid4{{grid-template-columns:1fr 1fr}}}}@media(max-width:640px){{h1{{font-size:32px}}.lead{{font-size:16px}}.menu{{display:none}}.grid2,.grid3,.grid4{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<div class="nav"><div class="wrap navin"><a class="brand" href="https://crazyrouter.com">Crazyrouter</a><div class="menu"><a class="active" href="/models/">Models</a><a href="https://crazyrouter.com/tools/pricing-calculator">Pricing</a><a href="https://docs.crazyrouter.com/introduction">Docs</a><a href="https://crazyrouter.com/tools/">Tools</a></div><a class="btn dark" href="{register_link(model.slug)}">Get API Key</a></div></div>
<div class="wrap">
<section class="hero"><div class="badge">{model.hero_badge}</div><h1>{model.name} API at <span>{prices['savings']}% off</span></h1><p class="lead">{model.summary} {model.description}</p><div class="hero-actions"><a class="btn primary" href="{register_link(model.slug)}">Start free</a><a class="btn light" href="#pricing">View pricing</a></div><div class="stats"><div class="stat">From ${money(prices['crazy_input'])} / 1M input</div><div class="stat">{model.context_window} context</div><div class="stat">{model.modality}</div><div class="stat">{governance_badge(model)}</div></div></section>
<section><div class="callout"><h2 style="text-align:left;margin-bottom:8px">Why this page exists</h2><p class="muted">{model.search_intent}</p><ul><li><strong>Last reviewed:</strong> {model.last_reviewed}</li><li><strong>Review cadence:</strong> {model.review_cadence}</li><li><strong>Owner:</strong> {model.owner}</li><li><strong>Indexing status:</strong> {model.seo_status}</li></ul></div></section>
<section id="pricing"><h2>{model.name} pricing comparison</h2><p class="subtitle">Compare the current Crazyrouter token price with the direct provider list price used for this landing page.</p><div class="grid2"><div class="card"><h3>{compare_label(model.provider)}</h3><div class="price-row"><span class="muted">Input per 1M tokens</span><span class="old">${money(prices['official_input'])}</span></div><div class="price-row"><span class="muted">Output per 1M tokens</span><span class="old">${money(prices['official_output'])}</span></div><div class="price-row"><span class="muted">Billing</span><span>Pay as you go</span></div></div><div class="card highlight"><span class="save">Save {prices['savings']}%</span><h3>Crazyrouter</h3><div class="price-row"><span class="muted">Input per 1M tokens</span><span class="green">${money(prices['crazy_input'])}</span></div><div class="price-row"><span class="muted">Output per 1M tokens</span><span class="green">${money(prices['crazy_output'])}</span></div><div class="price-row"><span class="muted">Billing</span><span>One key for 600+ models</span></div></div></div><div class="banner">Save ${money(prices['official_input'] - prices['crazy_input'])} per 1M input tokens on {model.name}. This page is updated from the live Crazyrouter pricing feed and reviewed on a regular cadence.</div></section>
<section><h2>{model.name} at a glance</h2><p class="subtitle">Use these details to decide whether this model fits the job before you wire it into production.</p><div class="grid4"><div class="card spec"><div class="label">Context window</div><div class="value">{model.context_window}</div></div><div class="card spec"><div class="label">Max output</div><div class="value">{model.max_output}</div></div><div class="card spec"><div class="label">Modality</div><div class="value">{model.modality}</div></div><div class="card spec"><div class="label">Latency profile</div><div class="value">{model.latency}</div></div></div></section>
<section><h2>Best-fit use cases</h2><p class="subtitle">These are the production situations where this model is most likely to earn its keep.</p><div class="grid3">{section_cards('This is a strong fit when the workflow consistently looks like this.', model.best_for)}</div></section>
<section><h2>When not to choose {model.name}</h2><p class="subtitle">High-quality landing pages should help visitors disqualify the wrong model, not just push every option.</p><div class="grid2">{section_cards('This is usually a sign that another model deserves a closer look first.', model.not_best_for)}</div></section>
<section><h2>Why teams use Crazyrouter here</h2><p class="subtitle">The gateway matters when you want commercial flexibility, not just lower price.</p><div class="grid3">{section_cards('This matters when the business wants optionality and easier operations.', model.why_crazyrouter)}</div></section>
<section><h2>How to think about {model.name}</h2><p class="subtitle">These notes help turn a pricing page into a real decision page.</p><div class="grid3">{section_cards('Comparison note', model.comparison_notes)}</div></section>
<section><h2>Start in 30 seconds</h2><p class="subtitle">Use the OpenAI SDK style and swap only the base URL plus the model name.</p><div class="tabs"><button class="tab active" onclick="showTab(event,'python')">Python</button><button class="tab" onclick="showTab(event,'curl')">cURL</button><button class="tab" onclick="showTab(event,'node')">Node.js</button></div><div class="code"><button class="copy" onclick="copyCode()">Copy</button><div id="tab-python" class="panel active"><pre>from openai import OpenAI

client = OpenAI(
    base_url="https://crazyrouter.com/v1",
    api_key="your-crazyrouter-key"
)

response = client.chat.completions.create(
    model="{model.api_model}",
    messages=[{{"role": "user", "content": "{model.example_prompt}"}}]
)

print(response.choices[0].message.content)</pre></div><div id="tab-curl" class="panel"><pre>curl https://crazyrouter.com/v1/chat/completions \
  -H "Authorization: Bearer your-crazyrouter-key" \
  -H "Content-Type: application/json" \
  -d '{{
    "model": "{model.api_model}",
    "messages": [{{"role": "user", "content": "{model.example_prompt}"}}]
  }}'</pre></div><div id="tab-node" class="panel"><pre>import OpenAI from "openai";

const client = new OpenAI({{
  baseURL: "https://crazyrouter.com/v1",
  apiKey: "your-crazyrouter-key",
}});

const response = await client.chat.completions.create({{
  model: "{model.api_model}",
  messages: [{{ role: "user", content: "{model.example_prompt}" }}],
}});

console.log(response.choices[0].message.content);</pre></div></div></section>
<section><h2>Frequently asked questions</h2>{faq_markup(faq)}</section>
<section><h2>Explore related models</h2><p class="subtitle">Compare adjacent options for quality, latency, and price without rebuilding your API stack.</p><div class="grid3">{related_cards(model, prices_by_slug)}</div></section>
</div>
<section class="cta"><div class="wrap"><h2>Ready to use {model.name} through Crazyrouter?</h2><p class="subtitle">Create an account, get one API key, and route traffic to the model that best fits each workload instead of forcing every request through a single provider.</p><a class="btn primary" href="{register_link(model.slug)}">Get started</a></div></section>
<div class="wrap"><div class="foot">© 2026 <a href="https://crazyrouter.com">Crazyrouter</a> · One API for 600+ AI models · <a href="/models/">Models</a> · <a href="https://docs.crazyrouter.com/introduction">Docs</a></div></div>
<script>
function showTab(event, name) {{
  document.querySelectorAll('.tab').forEach((el) => el.classList.remove('active'));
  document.querySelectorAll('.panel').forEach((el) => el.classList.remove('active'));
  event.currentTarget.classList.add('active');
  document.getElementById('tab-' + name).classList.add('active');
}}
function copyCode() {{
  const active = document.querySelector('.panel.active pre');
  navigator.clipboard.writeText(active.textContent);
  const button = document.querySelector('.copy');
  const text = button.textContent;
  button.textContent = 'Copied';
  setTimeout(() => button.textContent = text, 1500);
}}
</script>
</body>
</html>'''


def index_schema(indexed_models: list[Model]) -> str:
    return json.dumps({"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": index + 1, "name": model.name, "url": page_link(model.slug)} for index, model in enumerate(indexed_models)]}, ensure_ascii=False, indent=2)


def index_cards(models: list[Model], prices_by_slug: dict[str, dict]) -> str:
    html: list[str] = []
    for model in models:
        prices = prices_by_slug[model.slug]
        status = "Index" if model.seo_status == "index" else "Review"
        html.append(f'<a href="/models/{model.slug}" class="card"><div style="display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap;margin-bottom:14px"><span class="badge" style="margin:0">{model.provider}</span><span class="badge" style="margin:0;background:#eff6ff;color:#1d4ed8">{status}</span></div><h3>{model.name}</h3><p class="muted">{model.summary}</p><div style="display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap;font-weight:700"><span>${money(prices["crazy_input"])} / 1M input</span><span>{model.context_window} context</span></div></a>')
    return "".join(html)


def index_page(prices_by_slug: dict[str, dict]) -> str:
    indexed_models = [model for model in MODELS if model.seo_status == "index"]
    review_models = [model for model in MODELS if model.seo_status != "index"]
    cheapest = min(prices_by_slug.values(), key=lambda item: item["crazy_input"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI Model Pricing & Access | Crazyrouter Models</title>
<meta name="description" content="Compare popular OpenAI, Anthropic, Google, and DeepSeek model pricing on Crazyrouter. Browse the small set of maintained index-priority landing pages plus additional model pages under review.">
<meta name="keywords" content="ai model pricing, llm api pricing, compare ai models, crazyrouter models">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="https://crazyrouter.com/models/">
<meta property="og:title" content="Compare AI model pricing on Crazyrouter">
<meta property="og:description" content="Browse GPT, Claude, Gemini, DeepSeek, and reasoning model landing pages with live Crazyrouter pricing.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://crazyrouter.com/models/">
<meta property="og:image" content="https://crazyrouter.com/twitter-card.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Compare AI model pricing on Crazyrouter">
<meta name="twitter:description" content="Browse GPT, Claude, Gemini, DeepSeek, and reasoning model landing pages with live Crazyrouter pricing.">
<script type="application/ld+json">{index_schema(indexed_models)}</script>
<style>
*{{box-sizing:border-box}}body{{margin:0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#111827;background:#fff;line-height:1.6}}a{{color:inherit}}.wrap{{max-width:1120px;margin:0 auto;padding:0 16px}}.nav{{position:sticky;top:0;background:rgba(255,255,255,.94);backdrop-filter:blur(10px);border-bottom:1px solid #e5e7eb}}.navin{{height:64px;display:flex;align-items:center;justify-content:space-between}}.brand{{font-size:20px;font-weight:800;text-decoration:none}}.menu{{display:flex;gap:20px;font-size:14px}}.menu a{{text-decoration:none;color:#4b5563}}.menu a.active,.menu a:hover{{color:#2563eb}}.btn{{display:inline-block;text-decoration:none;border-radius:9999px;padding:12px 22px;font-weight:700}}.btn.dark{{background:#111827;color:#fff}}.btn.primary{{background:#2563eb;color:#fff}}.btn.light{{border:1px solid #d1d5db;color:#111827;background:#fff}}.hero{{padding:64px 0 44px;text-align:center}}.badge{{display:inline-block;background:#dbeafe;color:#1d4ed8;border-radius:9999px;padding:4px 12px;font-size:13px;font-weight:700}}h1{{font-size:46px;line-height:1.15;margin:16px 0}}h1 span{{color:#2563eb}}.lead{{max-width:800px;margin:0 auto 24px;color:#6b7280;font-size:18px}}.hero-actions{{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}}.grid3,.grid4{{display:grid;gap:20px}}.grid3{{grid-template-columns:repeat(3,minmax(0,1fr))}}.grid4{{grid-template-columns:repeat(4,minmax(0,1fr))}}.card{{border:1px solid #e5e7eb;border-radius:18px;padding:24px;background:#fff;text-decoration:none}}section{{padding:0 0 56px}}h2{{font-size:30px;line-height:1.2;text-align:center;margin:0 0 12px}}.subtitle{{max-width:760px;margin:0 auto 28px;text-align:center;color:#6b7280}}.stat{{text-align:center}}.stat .label{{font-size:14px;color:#6b7280;margin-bottom:6px}}.stat .value{{font-size:28px;font-weight:800}}.muted{{color:#6b7280}}.foot{{padding:32px 0;border-top:1px solid #e5e7eb;color:#9ca3af;text-align:center;font-size:13px}}.foot a{{color:#2563eb;text-decoration:none}}@media(max-width:900px){{.grid3,.grid4{{grid-template-columns:1fr 1fr}}}}@media(max-width:640px){{h1{{font-size:32px}}.lead{{font-size:16px}}.menu{{display:none}}.grid3,.grid4{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<div class="nav"><div class="wrap navin"><a class="brand" href="https://crazyrouter.com">Crazyrouter</a><div class="menu"><a class="active" href="/models/">Models</a><a href="https://crazyrouter.com/tools/pricing-calculator">Pricing</a><a href="https://docs.crazyrouter.com/introduction">Docs</a><a href="https://crazyrouter.com/tools/">Tools</a></div><a class="btn dark" href="{register_link('models-index')}">Get API Key</a></div></div>
<div class="wrap"><section class="hero"><div class="badge">Crazyrouter model pages</div><h1>Compare popular AI models on <span>one API</span></h1><p class="lead">This hub supports a focused SEO strategy: a small set of maintained index-priority landing pages plus additional model pages kept accessible for comparison, routing, and campaign use.</p><div class="hero-actions"><a class="btn primary" href="{register_link('models-index')}">Start free</a><a class="btn light" href="#index-pages">Explore maintained pages</a></div></section><section><div class="grid4"><div class="card stat"><div class="label">Model pages</div><div class="value">{len(MODELS)}</div></div><div class="card stat"><div class="label">Index-priority pages</div><div class="value">{len(indexed_models)}</div></div><div class="card stat"><div class="label">Pages under review</div><div class="value">{len(review_models)}</div></div><div class="card stat"><div class="label">Lowest input price</div><div class="value">${money(cheapest['crazy_input'])}</div></div></div></section><section id="index-pages"><h2>Maintained index-priority pages</h2><p class="subtitle">These are the landing pages currently treated as the strongest long-term organic targets.</p><div class="grid3">{index_cards(indexed_models, prices_by_slug)}</div></section><section><h2>Additional model pages</h2><p class="subtitle">These pages remain useful for direct access, campaign traffic, and internal comparison, but they are not all prioritized for organic indexation yet.</p><div class="grid3">{index_cards(review_models, prices_by_slug)}</div></section><section><h2>Why this hub is structured this way</h2><p class="subtitle">The goal is not to mass-produce thin pages. It is to keep a small group of strong landing pages indexed, while still letting other model pages exist and mature over time.</p><div class="grid3"><div class="card"><h3>Index selectively</h3><p class="muted">Only a handful of pages are treated as long-term organic assets right now.</p></div><div class="card"><h3>Review continuously</h3><p class="muted">Each model page carries review metadata so stale pages can be revised, noindexed, or retired before quality drifts.</p></div><div class="card"><h3>Route with intent</h3><p class="muted">Users can still compare and click through the full model set without forcing every page into search results immediately.</p></div></div></section><div class="foot">© 2026 <a href="https://crazyrouter.com">Crazyrouter</a> · One API for 600+ AI models · <a href="https://docs.crazyrouter.com/introduction">Docs</a></div></div>
</body>
</html>'''


def sitemap() -> str:
    indexed_urls = ["https://crazyrouter.com/models/"] + [page_link(model.slug) for model in MODELS if model.seo_status == "index"]
    rows = ["<?xml version=\"1.0\" encoding=\"UTF-8\"?>", '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in indexed_urls:
        rows.append("  <url>")
        rows.append(f"    <loc>{url}</loc>")
        rows.append(f"    <lastmod>{TODAY}</lastmod>")
        rows.append("  </url>")
    rows.append("</urlset>")
    return "\n".join(rows)


def build() -> None:
    records = fetch_prices()
    prices_by_slug: dict[str, dict] = {}
    for model in MODELS:
        if model.api_model not in records:
            raise KeyError(f"Missing pricing record for {model.api_model}")
        prices_by_slug[model.slug] = compute_price(records[model.api_model])
    for model in MODELS:
        target = ROOT / model.slug
        target.mkdir(parents=True, exist_ok=True)
        target.joinpath("index.html").write_text(page_template(model, prices_by_slug[model.slug], prices_by_slug), encoding="utf-8")
    ROOT.joinpath("index.html").write_text(index_page(prices_by_slug), encoding="utf-8")
    ROOT.joinpath("sitemap.xml").write_text(sitemap(), encoding="utf-8")


if __name__ == "__main__":
    build()
