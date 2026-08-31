import { useFeedStore } from "../../store/feed_store";
import styles from "./FollowButton.module.scss";

interface FollowButtonProps {
  userId: string;
  followed: boolean;
}

export function FollowButton({ userId, followed }: FollowButtonProps) {
  const toggleFollow = useFeedStore((state) => state.toggleFollow);

  return (
    <button
      type="button"
      className={followed ? `${styles.button} ${styles.following}` : styles.button}
      onClick={() => void toggleFollow(userId)}
    >
      {followed ? "Following" : "Follow"}
    </button>
  );
}
