import { copyFileSync, existsSync, mkdirSync, readSync, statSync, openSync, closeSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const sourcePath = new URL('./entry.png', import.meta.url);
const sourceFilePath = fileURLToPath(sourcePath);

if (!existsSync(sourceFilePath)) {
  console.error(`Error: Source file ${sourceFilePath} does not exist.`);
  process.exit(1);
}

// Validate PNG signature: 89 50 4E 47 0D 0A 1A 0A
const PNG_SIGNATURE = Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]);
const buffer = Buffer.alloc(8);
let fd;
try {
  fd = openSync(sourceFilePath, 'r');
  readSync(fd, buffer, 0, 8, 0);
} catch (err) {
  console.error('Error reading source file signature:', err);
  process.exit(1);
} finally {
  if (fd !== undefined) {
    try {
      closeSync(fd);
    } catch {}
  }
}

if (!buffer.equals(PNG_SIGNATURE)) {
  console.error('Error: entry.png is not a valid PNG file (invalid signature).');
  process.exit(1);
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const destPath = join(outDir, 'entry.png');

try {
  mkdirSync(outDir, { recursive: true });
  copyFileSync(sourcePath, destPath);
  const stats = statSync(destPath);
  console.log(`Successfully validated and copied entry.png to ${destPath} (${stats.size} bytes)`);
} catch (err) {
  console.error('Error copying entry.png:', err);
  process.exit(1);
}
