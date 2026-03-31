const crypto = require("crypto");

const idGenerate = () => {
    // lets generate (128 bits) 16 random bytes
    const bytes = new Uint8Array(16);
    crypto.getRandomValues(bytes);

    // Set the version to 4 (0100 in bits) at the 7th byte
    bytes[6] = (bytes[6] & 0x0f) | 0x40;

    // Set the variant to RFC 4122 (10xx in bits) at the 9th byte
    bytes[8] = (bytes[8] & 0x3f) | 0x80;

    // Convert to hex string and format with hyphens (8-4-4-4-12)
    const hex = Array.from(bytes)
        .map(b => b.toString(16).padStart(2, '0'))
        .join('');

    return `${hex.slice(0, 8)}-${hex.slice(8, 12)}-${hex.slice(12, 16)}-${hex.slice(16, 20)}-${hex.slice(20)}`;
};


console.log(idGenerate());

module.exports={idGenerate}