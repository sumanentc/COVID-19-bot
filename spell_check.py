import typing
from typing import Any, Optional, Text, Dict, List, Type

from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.shared.nlu.training_data.message import Message
from spellchecker import SpellChecker

spell = SpellChecker()
spell.word_frequency.load_words(
    [
        "Andhra",
        "Pradesh",
        "Arunachal",
        "Assam",
        "Bihar",
        "Chhattisgarh",
        "Gujarat",
        "Haryana",
        "Himachal",
        "Jharkhand",
        "Karnataka",
        "Kerala",
        "Madhya",
        "Maharashtra",
        "Manipur",
        "Meghalaya",
        "Mizoram",
        "Nagaland",
        "Odisha",
        "Sikkim",
        "Nadu",
        "Telangana",
        "Tripura",
        "Uttarakhand",
        "Uttar",
        "Bengal",
        "WB",
        "MP",
        "UP",
        "ind",
        "Adilabad",
        "Agar",
        "Agatti",
        "Ahmednagar",
        "Akola",
        "Amravati",
        "Aurangabad",
        "Beed",
        "Bhandara",
        "Buldhana",
        "Chandrapur",
        "Dhule",
        "Gadchiroli",
        "Gondia",
        "Hingoli",
        "Jalgaon",
        "Jalna",
        "Kolhapur",
        "Latur",
        "Nagpur",
        "Nanded",
        "Nandurbar",
        "Nashik",
        "Osmanabad",
        "Palghar",
        "Parbhani",
        "Pune",
        "Raigad",
        "Ratnagiri",
        "Sangli",
        "Satara",
        "Sindhudurg",
        "Solapur",
        "Thane",
        "Wardha",
        "Washim",
        "Yavatmal",
        "Alipurduar",
        "District",
        "Bankura",
        "Basirhat",
        "Parganas",
        "Birbhum",
        "Bishnupur",
        "Bankura",
        "Cooch",
        "Behar",
        "COOCHBEHAR",
        "Dakshin",
        "Dinajpur",
        "Darjeeling",
        "Harbor",
        "Bardhaman",
        "Hoogly",
        "Howrah",
        "Jalpaiguri",
        "Jhargram",
        "Kalimpong",
        "Kolkata",
        "Malda",
        "Murshidabad",
        "Nadia",
        "Nandigram",
        "Medinipore",
        "Parganas",
        "Paschim",
        "Medinipore",
        "Purba",
        "Purulia",
        "Rampurhat",
        "Birbhum",
        "Uttar",
        "Dinajpur",
        "Bardhaman",
        "(Bankura)",
        "Bishnupur HD (Bankura)",
        "Cooch Behar",
        "(S 24 Parganas)",
        "(East Medinipore)",
        "(Birbhum)",
    ]
)
spell.known(
    [
        "Andhra",
        "Pradesh",
        "Arunachal",
        "Assam",
        "Bihar",
        "Chhattisgarh",
        "Gujarat",
        "Haryana",
        "Himachal",
        "Jharkhand",
        "Karnataka",
        "Kerala",
        "Madhya",
        "Maharashtra",
        "Manipur",
        "Meghalaya",
        "Mizoram",
        "Nagaland",
        "Odisha",
        "Sikkim",
        "Nadu",
        "Telangana",
        "Tripura",
        "Uttarakhand",
        "Uttar",
        "Bengal",
        "WB",
        "MP",
        "UP",
        "ind",
        "Adilabad",
        "Agar",
        "Agatti",
        "Ahmednagar",
        "Akola",
        "Amravati",
        "Aurangabad",
        "Beed",
        "Bhandara",
        "Buldhana",
        "Chandrapur",
        "Dhule",
        "Gadchiroli",
        "Gondia",
        "Hingoli",
        "Jalgaon",
        "Jalna",
        "Kolhapur",
        "Latur",
        "Nagpur",
        "Nanded",
        "Nandurbar",
        "Nashik",
        "Osmanabad",
        "Palghar",
        "Parbhani",
        "Pune",
        "Raigad",
        "Ratnagiri",
        "Sangli",
        "Satara",
        "Sindhudurg",
        "Solapur",
        "Thane",
        "Wardha",
        "Washim",
        "Yavatmal",
        "Alipurduar",
        "District",
        "Bankura",
        "Basirhat",
        "Parganas",
        "Birbhum",
        "Bishnupur",
        "Bankura",
        "Cooch",
        "Behar",
        "COOCHBEHAR",
        "Dakshin",
        "Dinajpur",
        "Darjeeling",
        "Harbor",
        "Bardhaman",
        "Hoogly",
        "Howrah",
        "Jalpaiguri",
        "Jhargram",
        "Kalimpong",
        "Kolkata",
        "Malda",
        "Murshidabad",
        "Nadia",
        "Nandigram",
        "Medinipore",
        "Parganas",
        "Paschim",
        "Medinipore",
        "Purba",
        "Purulia",
        "Rampurhat",
        "Birbhum",
        "Uttar",
        "Dinajpur",
        "Bardhaman",
        "(Bankura)",
        "Bishnupur HD (Bankura)",
        "Cooch Behar",
        "(S 24 Parganas)",
        "(East Medinipore)",
        "(Birbhum)",
    ]
)

if typing.TYPE_CHECKING:
    from rasa.nlu.model import Metadata


class CorrectSpelling(Component):
    """A new component"""

    # Which components are required by this component.
    # Listed components should appear before the component itself in the pipeline.
    @classmethod
    def required_components(cls) -> List[Type[Component]]:
        """Specify which components need to be present in the pipeline."""

        return []

    # Defines the default configuration parameters of a component
    # these values can be overwritten in the pipeline configuration
    # of the model. The component should choose sensible defaults
    # and should be able to create reasonable results with the defaults.
    defaults = {}

    # Defines what language(s) this component can handle.
    # This attribute is designed for instance method: `can_handle_language`.
    # Default value is None which means it can handle all languages.
    # This is an important feature for backwards compatibility of components.
    supported_language_list = ["en"]

    # Defines what language(s) this component can NOT handle.
    # This attribute is designed for instance method: `can_handle_language`.
    # Default value is None which means it can handle all languages.
    # This is an important feature for backwards compatibility of components.
    not_supported_language_list = None

    def __init__(self, component_config: Optional[Dict[Text, Any]] = None) -> None:
        super().__init__(component_config)

    def train(
        self,
        training_data: TrainingData,
        config: Optional[RasaNLUModelConfig] = None,
        **kwargs: Any,
    ) -> None:
        """Train this component.

        This is the components chance to train itself provided
        with the training data. The component can rely on
        any context attribute to be present, that gets created
        by a call to :meth:`components.Component.pipeline_init`
        of ANY component and
        on any context attributes created by a call to
        :meth:`components.Component.train`
        of components previous to this one."""
        pass

    def process(self, message: Message, **kwargs: Any) -> None:
        """Process an incoming message.

        This is the components chance to process an incoming
        message. The component can rely on
        any context attribute to be present, that gets created
        by a call to :meth:`components.Component.pipeline_init`
        of ANY component and
        on any context attributes created by a call to
        :meth:`components.Component.process`
        of components previous to this one."""

        try:
            textdata = message.data["text"]
            # print("text :::" + textdata)
            textdata = textdata.split()
            new_message = " ".join(spell.correction(w) for w in textdata)
            # print("after correction text :::" + new_message)
            message.data["text"] = new_message
        except KeyError:
            pass

    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        """Persist this component to disk for future loading."""

        pass

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir: Optional[Text] = None,
        model_metadata: Optional["Metadata"] = None,
        cached_component: Optional["Component"] = None,
        **kwargs: Any,
    ) -> "Component":
        """Load this component from file."""

        if cached_component:
            return cached_component
        else:
            return cls(meta)
