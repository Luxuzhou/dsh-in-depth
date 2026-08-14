import Schema from '@deepseek-ai/schemastery'
import { defineTool } from '@deepseek-ai/dsh-tools'

export const name = 'book-greet-tool'
export const inject = ['tools']

export const Config = Schema.object({
  greeting: Schema.string().default('Hello'),
})

export function apply(ctx, config) {
  ctx.tools.register(defineTool({
    name: 'greet',
    description: 'Greet one person by name when the user explicitly asks for a greeting.',
    parameters: {
      name: {
        type: 'string',
        required: true,
        description: 'The person name to include in the greeting.',
      },
    },
    output: {
      schema: { type: 'string' },
      render: (_args, value) => [{ type: 'text', text: value }],
    },
    async execute(args) {
      return `${config.greeting}, ${args.name}!`
    },
  }))
}
