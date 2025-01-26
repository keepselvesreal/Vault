import pytest

class TestMediumCrawler:
    @pytet.fixture
    def test_extract(self, link: str, **kwargs, model) -> None:
        old_model = self.model.find(link=link)
        if old_model is not None:
            # logger.info(f"Article already exists in the database: {link}")

            return


        self.driver.get(link)
        self.scroll_page()

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        title = soup.find_all("h1", class_="pw-post-title")
        subtitle = soup.find_all("h2", class_="pw-subtitle-paragraph")

        data = {
            "Title": title[0].string if title else None,
            "Subtitle": subtitle[0].string if subtitle else None,
            "Content": soup.get_text(),
        }

        self.driver.close()

        user = kwargs["user"]
        instance = model(
            platform="medium",
            content=data,
            link=link,
            author_id=user.id,
            author_full_name=user.full_name,
        )
        instance.save()

        logger.info(f"Successfully scraped and saved article: {link}")