import { NextRequest, NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  const { message } = await req.json();
  const host = process.env.OLLAMA_HOST || 'http://localhost:11434';
  const res = await fetch(`${host}/api/generate`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ model: 'gpt-oss:20b', prompt: message }),
  });
  const data = await res.json();
  return NextResponse.json({ reply: data.response });
}
