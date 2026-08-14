import type { Context } from '@deepseek-ai/cordis'

export const name = 'book-session-observer'

export function apply(ctx: Context) {
  ctx.on('session/event', (session, event) => {
    // Deliberately avoid message bodies and tool content in teaching logs.
    console.log(JSON.stringify({
      sessionId: session.id,
      seq: event.seq,
      type: event.type,
    }))
  })
}
