import scrape_wiki
import requests as req


pass_fail = {
    True: "PASS✅", 
    False: "FAIL🖕",
}

test_writer = (lambda t: 
               (lambda c: 
                (lambda r: 
                 f"{pass_fail[r]} {t}: {c}")))

test_cases = (lambda writer:
    (lambda f:
        (lambda case, expected:
         [[writer(c)(f(c) == e), f(c) == e] 
          for c, e in zip(case, expected)])))



class Test:

    def __init__(self):
        self.content = req.get("https://en.wikipedia.org/wiki/Wikipedia")  
        self.passed = 0
        self.failed = 0
        self.total_tested = 0

    def test(self, writer, func, cases, expected):
        for r in test_cases(writer)(func)(cases, expected):
            self.total_tested += 1
            print(r[0])
            if r[1]:
                self.test_passed()
            else:
                self.test_failed()

        print("")


    def is_media_test(self):
        writer = test_writer("is_media")
        cases = [
            "http://random-stuff.jpg",
            "http://random-stuff.PDF",
            "http://random-stuff.jpeg",
            "http://random-stuff.com",
            "http://random-stuff.html",
        ]
        expected = [
            True,
            True,
            True,
            False,
            False,
        ]
        self.test(writer, scrape_wiki.is_media, cases, expected)


    def is_internal_link_test(self):
        writer = test_writer("is_internal_link")
        cases = [
            "//www.random-stuff.com",
            "https://random-stuff.PDF",
            "/random-stuff.jpeg",
            "/random-stuff.com",
            "http://random-stuff.org",
        ]
        expected = [
            False,
            False,
            False,
            True,
            False,
        ]
        self.test(writer, scrape_wiki.is_internal_link, cases, expected)

    def is_external_link_test(self):
        writer = test_writer("is_external_link")
        cases = [
            "//www.random-stuff.com",
            "https://random-stuff.PDF",
            "/random-stuff.jpeg",
            "/random-stuff.com",
            "http://random-stuff.org",
        ]
        expected = [
            True,
            False,
            False,
            False,
            True,
        ]
        self.test(writer, scrape_wiki.is_external_link, cases, expected)

    def is_internal_media_test(self):
        writer = test_writer("is_internal_media")
        cases = [
            "//www.random-stuff.com",
            "https://random-stuff.PDF",
            "/random-stuff.jpeg",
            "/random-stuff.com",
            "http://random-stuff.JPG",
        ]
        expected = [
            False,
            False,
            True,
            False,
            False,
        ]
        self.test(writer, scrape_wiki.is_internal_media, cases, expected)

    def is_external_media_test(self):
        writer = test_writer("is_external_media")
        cases = [
            "//www.random-stuff.com",
            "https://random-stuff.PDF",
            "/random-stuff.jpeg",
            "/random-stuff.com",
            "http://random-stuff.JPG",
        ]
        expected = [
            False,
            True,
            False,
            False,
            True,
        ]
        self.test(writer, scrape_wiki.is_external_media, cases, expected)
    
    def is_not_none_test(self):
        writer = test_writer("is_external_media")
        cases = [
            "//www.random-stuff.com",
            "None",
            "https://random-stuff.org",
            "/random-stuff.com",
            "some-img.png",
        ]
        expected = [
            True,
            False,
            True,
            True,
            True,
        ]
        self.test(writer, scrape_wiki.is_not_none, cases, expected)

    def is_citation_test(self):
        writer = test_writer("is_citation")
        cases = [
            "//www.random-stuff.com",
            "#some-paragragh",
            "https://random-stuff.org",
            "/random-stuff.com",
            "#something",
        ]
        expected = [
            False,
            True,
            False,
            False,
            True,
        ]
        self.test(writer, scrape_wiki.is_citation, cases, expected)

    def get_soup_test(self):
        pass

    def get_body_test(self):
        pass

    def process_response_test(self):
        pass

    def get_href_test(self):
        pass

    def page_urls_test(self):
        pass

    def internal_links_test(self):
        pass

    def external_links_test(self):
        pass

    def internal_media_test(self):
        pass

    def external_media_test(self):
        pass

    def citations_test(self):
        pass

    def get_wiki_content_test(self):
        pass

    def scrape_wiki_test(self):
        pass

    def test_passed(self):
        self.passed += 1

    def test_failed(self):
        self.failed += 1

    def run(self):
        self.is_media_test()
        self.is_internal_link_test()
        self.is_external_link_test()
        self.is_internal_media_test()
        self.is_external_media_test()
        self.is_not_none_test()
        self.is_citation_test()
        print(f"Total test: {self.total_tested}")
        print(f"Total passed: {self.passed}")
        print(f"Total failed: {self.failed}")


if __name__ == "__main__":

    Test().run()
