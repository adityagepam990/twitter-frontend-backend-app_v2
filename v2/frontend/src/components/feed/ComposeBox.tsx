import { useRef, useState } from "react";
import type { ChangeEvent } from "react";

import type { ApiError } from "../../api/client";
import { useFeedStore } from "../../store/feed_store";
import { Avatar } from "../ui/Avatar";
import styles from "./ComposeBox.module.scss";

const WARNING_THRESHOLD = 260;
const MAX_LENGTH = 280;

function errorMessage(error: unknown): string {
  if (error && typeof error === "object" && "detail" in error) {
    return String((error as ApiError).detail);
  }
  return "Something went wrong.";
}

export function ComposeBox() {
  const submitPost = useFeedStore((state) => state.submitPost);
  const [text, setText] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const handleChange = (event: ChangeEvent<HTMLTextAreaElement>) => {
    setText(event.target.value);
    setError(null);

    const textarea = textareaRef.current;
    if (textarea) {
      textarea.style.height = "auto";
      textarea.style.height = `${textarea.scrollHeight}px`;
    }
  };

  const handleSubmit = async () => {
    setIsSubmitting(true);
    setError(null);
    try {
      await submitPost(text);
      setText("");
      const textarea = textareaRef.current;
      if (textarea) {
        textarea.style.height = "auto";
      }
    } catch (submitError) {
      setError(errorMessage(submitError));
    } finally {
      setIsSubmitting(false);
    }
  };

  const count = text.length;
  const isOverLimit = count > MAX_LENGTH;
  const isEmpty = text.trim().length === 0;

  return (
    <div className={styles.compose}>
      <Avatar src="" displayName="Pulse User" size="md" />

      <div className={styles.body}>
        <textarea
          ref={textareaRef}
          className={styles.textarea}
          placeholder="What's happening?"
          rows={1}
          value={text}
          onChange={handleChange}
        />

        {error && <p className={styles.error}>{error}</p>}

        <div className={styles.footer}>
          <span className={count >= WARNING_THRESHOLD ? `${styles.count} ${styles.warning}` : styles.count}>
            {count}/{MAX_LENGTH}
          </span>
          <button
            type="button"
            className={styles.postButton}
            disabled={isEmpty || isOverLimit || isSubmitting}
            onClick={() => void handleSubmit()}
          >
            Post
          </button>
        </div>
      </div>
    </div>
  );
}
