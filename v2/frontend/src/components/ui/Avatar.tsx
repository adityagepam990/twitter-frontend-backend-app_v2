import { useState } from "react";

import styles from "./Avatar.module.scss";

interface AvatarProps {
  src: string;
  displayName: string;
  size?: "sm" | "md" | "lg";
}

function getInitials(displayName: string): string {
  const words = displayName.trim().split(/\s+/).filter(Boolean);
  if (words.length === 0) {
    return "";
  }
  const first = words[0]![0] ?? "";
  const last = words.length > 1 ? (words[words.length - 1]![0] ?? "") : "";
  return `${first}${last}`.toUpperCase();
}

export function Avatar({ src, displayName, size = "md" }: AvatarProps) {
  const [failed, setFailed] = useState(false);

  if (failed) {
    return (
      <div className={`${styles.avatar} ${styles[size]}`} role="img" aria-label={displayName}>
        {getInitials(displayName)}
      </div>
    );
  }

  return (
    <img
      className={`${styles.avatar} ${styles[size]}`}
      src={src}
      alt={displayName}
      onError={() => setFailed(true)}
    />
  );
}
