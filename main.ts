import { copyFileSync, mkdirSync, statSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const sourcePath = new URL('./entry.png', import.meta.url);
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const destPath = join(outDir, 'entry.png');

try {
  mkdirSync(outDir, { recursive: true });
  copyFileSync(sourcePath, destPath);
  const stats = statSync(destPath);
  console.log(`Copied entry.png to ${destPath} (${stats.size} bytes)`);
} catch (err) {
  console.error('Error copying entry.png:', err);
  process.exit(1);
}
