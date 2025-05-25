## Overview

We get a ZIP file that contains a .lnk (Windows shortcut) file. These types of files can sometimes hide metadata or embedded content, so we investigate further.

### Step 1: Initial Analysis with `binwalk`

We started by running `binwalk` on the provided `gangster.zip` file to see what was inside and extract any embedded files.

```bash
binwalk -e gangster.zip
```

**Output:**

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v2.0 to extract, name: important_docs/
45            0x2D            Zip archive data, at least v2.0 to extract, compressed size: 1162, uncompressed size: 3025, name: important_docs/important_docs.lnk
1467          0x5BB           End of Zip archive, footer length: 22
```

This showed that the archive contained a directory named `important_docs/` and a `.lnk` file (Windows shortcut), which might contain hidden data.

---

### Step 2: Looking for Clues with `strings`

We used `strings` to inspect the extracted content and look for anything interesting:

```bash
strings _gangster.zip.extracted/0.zip
```

**Interesting output:**

```
...
important_docs/important_docs.lnk
...
;DEFGZmxhZ3thZjExNTBmMDdmOTAwODcyZTE2MmUyMzBkMGVmOGY5NH0K
...
```

We found a suspicious Base64-encoded string:

```
DEFGZmxhZ3thZjExNTBmMDdmOTAwODcyZTE2MmUyMzBkMGVmOGY5NH0K
```

---

### Step 3: Decoding the Flag

We decoded the string using `base64`:

```bash
echo "DEFGZmxhZ3thZjExNTBmMDdmOTAwODcyZTE2MmUyMzBkMGVmOGY5NH0K" | base64 -d
```

**Output:**

```
flag{**************************************}
```

---

