def render_start(title: str, subtitle: str, has_screenshot: bool) -> str:
    status = "✅ Скриншот получен" if has_screenshot else "📸 Скриншот ещё не отправлен"

    return (
        f"{title}\n\n"
        f"<blockquote>{subtitle}</blockquote>\n\n"
        f"<b>Статус:</b> {status}"
    )
