#!/usr/bin/env python3

from dataclasses import dataclass


# ──────────────────────────────────────────────────────────────────────────────
# Data Model
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class FileEntry:
    offset:      int    # byte offset where the signature starts
    signature:   bytes  # raw bytes to match
    file_type:   str    # human-readable type name
    extension:   str    # typical file extension(s)
    description: str    # extra detail


# ──────────────────────────────────────────────────────────────────────────────
# File Signature Database
# ──────────────────────────────────────────────────────────────────────────────

def _h(hex_str: str) -> bytes:
    return bytes.fromhex(hex_str)


FILE_DATABASE: list[FileEntry] = [
    # ── Images ────────────────────────────────────────────────────────────────
    FileEntry(0, _h("474946383961"),         "GIF",          ".gif",               "GIF89a image"),
    FileEntry(0, _h("474946383761"),         "GIF",          ".gif",               "GIF87a image"),
    FileEntry(0, _h("89504E470D0A1A0A"),     "PNG",          ".png",               "PNG image"),
    FileEntry(0, _h("FFD8FF"),               "JPEG",         ".jpg",               "JPEG image"),
    FileEntry(0, _h("424D"),                 "BMP",          ".bmp",               "Bitmap image"),
    FileEntry(0, _h("49492A00"),             "TIFF",         ".tiff",              "TIFF image (little-endian)"),
    FileEntry(0, _h("4D4D002A"),             "TIFF",         ".tiff",              "TIFF image (big-endian)"),
    FileEntry(0, _h("52494646"),             "WEBP/AVI/WAV", ".riff",              "RIFF container (WebP/AVI/WAV)"),
    FileEntry(0, _h("00000100"),             "ICO",          ".ico",               "Windows Icon"),

    # ── Documents ─────────────────────────────────────────────────────────────
    FileEntry(0, _h("255044462D"),           "PDF",          ".pdf",               "PDF document"),
    FileEntry(0, _h("D0CF11E0A1B11AE1"),     "MS-CFB",       ".doc/.xls/.ppt",     "Microsoft Compound File (legacy Office)"),
    FileEntry(0, _h("504B0304"),             "ZIP/OOXML",    ".zip/.docx/.xlsx",   "ZIP / Office Open XML"),
    FileEntry(0, _h("7B5C727466"),           "RTF",          ".rtf",               "Rich Text Format"),

    # ── Archives ──────────────────────────────────────────────────────────────
    FileEntry(0, _h("526172211A0700"),       "RAR",          ".rar",               "RAR archive v1.5+"),
    FileEntry(0, _h("526172211A070100"),     "RAR5",         ".rar",               "RAR archive v5+"),
    FileEntry(0, _h("1F8B"),                 "GZIP",         ".gz",                "GZip compressed data"),
    FileEntry(0, _h("425A68"),               "BZIP2",        ".bz2",               "BZip2 compressed data"),
    FileEntry(0, _h("FD377A585A00"),         "XZ",           ".xz",                "XZ compressed data"),
    FileEntry(0, _h("377ABCAF271C"),         "7ZIP",         ".7z",                "7-Zip archive"),
    FileEntry(0, _h("1F9D"),                 "Z",            ".Z",                 "Unix compress (.Z)"),
    FileEntry(0, _h("04224D18"),             "LZ4",          ".lz4",               "LZ4 compressed data"),
    FileEntry(0, _h("28B52FFD"),             "ZSTD",         ".zst",               "Zstandard compressed data"),

    # ── Executables ───────────────────────────────────────────────────────────
    FileEntry(0, _h("4D5A"),                 "EXE/DLL",      ".exe/.dll",          "Windows PE executable"),
    FileEntry(0, _h("7F454C46"),             "ELF",          ".elf",               "Linux/Unix ELF executable"),
    FileEntry(0, _h("CAFEBABE"),             "CLASS/FAT",    ".class/.dylib",      "Java class file or Mach-O Fat binary"),
    FileEntry(0, _h("FEEDFACE"),             "MACHO32",      ".dylib/.o",          "Mach-O 32-bit binary"),
    FileEntry(0, _h("FEEDFACF"),             "MACHO64",      ".dylib/.o",          "Mach-O 64-bit binary"),

    # ── Audio / Video ─────────────────────────────────────────────────────────
    FileEntry(0, _h("494433"),               "MP3",          ".mp3",               "MP3 audio (ID3 tag)"),
    FileEntry(0, _h("FFFB"),                 "MP3",          ".mp3",               "MP3 audio (raw frame)"),
    FileEntry(0, _h("664C6143"),             "FLAC",         ".flac",              "FLAC audio"),
    FileEntry(0, _h("4F676753"),             "OGG",          ".ogg",               "Ogg container"),
    FileEntry(0, _h("1A45DFA3"),             "MKV/WEBM",     ".mkv/.webm",         "Matroska / WebM video"),
    FileEntry(4, _h("66747970"),             "MP4",          ".mp4",               "MP4 container (ftyp)"),
    FileEntry(0, _h("000001BA"),             "MPEG",         ".mpg",               "MPEG video stream"),
    FileEntry(0, _h("000001B3"),             "MPEG",         ".mpg",               "MPEG video stream"),

    # ── Crypto / Blockchain ───────────────────────────────────────────────────
    FileEntry(0, _h("D9B4BEF9"),             "BITCOIN_BLOCK",".blk",               "Bitcoin block magic"),

    # ── Text / Scripts ────────────────────────────────────────────────────────
    FileEntry(0, b"#!/",                     "SHEBANG_SCRIPT",".sh/.py/.rb",       "Unix script with shebang"),
    FileEntry(0, b"<?xml",                   "XML",          ".xml",               "XML document"),
    FileEntry(0, b"<?php",                   "PHP",          ".php",               "PHP script"),
    FileEntry(0, b"<!DOCTYPE",               "HTML",         ".html",              "HTML document"),
    FileEntry(0, b"<html",                   "HTML",         ".html",              "HTML document"),

    # ── Fonts ─────────────────────────────────────────────────────────────────
    FileEntry(0, _h("774F4646"),             "WOFF",         ".woff",              "Web Open Font Format"),
    FileEntry(0, _h("774F4632"),             "WOFF2",        ".woff2",             "Web Open Font Format 2"),

    # ── Database ──────────────────────────────────────────────────────────────
    FileEntry(0, _h("53514C69746520666F726D6174203300"), "SQLITE3", ".sqlite",     "SQLite 3 database"),
]

MAX_FILE_BYTES = 10 * 1024 * 1024


# ──────────────────────────────────────────────────────────────────────────────
# Identification Functions
# ──────────────────────────────────────────────────────────────────────────────

def identify_from_bytes(data: bytes) -> list[FileEntry]:
    matches = []
    for entry in FILE_DATABASE:
        if len(data) < entry.offset + len(entry.signature):
            continue
        
        if data.startswith(entry.signature, entry.offset):
            matches.append(entry)
    return matches


def scan_embedded(data: bytes) -> list[tuple[int, FileEntry]]:
    sigs = [(e, e.signature) for e in FILE_DATABASE if e.offset == 0]
    seen: set[tuple[int, str]] = set()
    results: list[tuple[int, FileEntry]] = []

    for pos in range(1, len(data)):
        for entry, sig in sigs:
            if data[pos:pos + len(sig)] == sig:
                key = (pos, entry.file_type)
                if key not in seen:
                    seen.add(key)
                    results.append((pos, entry))

    return results


# ──────────────────────────────────────────────────────────────────────────────
# Main API 
# ──────────────────────────────────────────────────────────────────────────────

def analyse(data: bytes, filename: str = "") -> dict:
    chunk = data[:MAX_FILE_BYTES]

    matches = [
        {
            "file_type":   m.file_type,
            "extension":   m.extension,
            "description": m.description,
            "icon":        "📄",
            "offset":      m.offset,
            "signature":   m.signature.hex().upper(),
        }
        for m in identify_from_bytes(chunk)
    ]

    embedded = [
        {
            "offset":      offset,
            "offset_hex":  f"0x{offset:08X}",
            "file_type":   m.file_type,
            "extension":   m.extension,
            "description": m.description,
            "icon":        "📄",
        }
        for offset, m in scan_embedded(chunk)
    ]

    return {
        "filename":  filename,
        "size":      len(data),
        "truncated": len(data) > MAX_FILE_BYTES,
        "matches":   matches,
        "embedded":  embedded,
    }