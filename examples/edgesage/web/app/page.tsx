'use client';

import { useEffect, useState } from 'react';

export default function Home() {
  const [history, setHistory] = useState<string[]>([]);
  const [input, setInput] = useState('');

  const send = async () => {
    if (!input) return;
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: input }),
    });
    const data = await res.json();
    setHistory((h) => [...h, `> ${input}`, data.reply]);
    setInput('');
  };

  return (
    <main>
      <h1>EdgeSage</h1>
      <div>
        <input value={input} onChange={(e) => setInput(e.target.value)} />
        <button onClick={send}>Send</button>
      </div>
      <pre>{history.join('\n')}</pre>
    </main>
  );
}
