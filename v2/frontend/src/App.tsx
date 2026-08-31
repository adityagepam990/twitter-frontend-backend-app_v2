import { AppLayout } from "./components/layout/AppLayout";
import { ComposeBox } from "./components/feed/ComposeBox";
import { FeedColumn } from "./components/feed/FeedColumn";

function App() {
  return (
    <AppLayout>
      <ComposeBox />
      <FeedColumn />
    </AppLayout>
  );
}

export default App;
