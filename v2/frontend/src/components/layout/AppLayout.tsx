import type { ReactNode } from "react";

import styles from "./AppLayout.module.scss";
import { LeftSidebar } from "./LeftSidebar";
import { RightSidebar } from "./RightSidebar";

interface AppLayoutProps {
  children: ReactNode;
}

export function AppLayout({ children }: AppLayoutProps) {
  return (
    <div className={styles.layout}>
      <aside className={styles.left}>
        <LeftSidebar />
      </aside>
      <main className={styles.center}>{children}</main>
      <aside className={styles.right}>
        <RightSidebar />
      </aside>
    </div>
  );
}
